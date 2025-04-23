import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key')

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # appetizer, main, dessert, etc.
    image_url = db.Column(db.String(255))
    is_available = db.Column(db.Boolean, default=True)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'image_url': self.image_url,
            'is_available': self.is_available,
            'featured': self.featured
        }

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    seating_type = db.Column(db.String(50), nullable=False)  # normal, family, party
    special_requests = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'date': self.date.strftime('%Y-%m-%d'),
            'time': self.time,
            'guests': self.guests,
            'seating_type': self.seating_type,
            'special_requests': self.special_requests,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='unread')  # unread, read, responded
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Routes
@app.route('/')
def index():
    return redirect('/Home Page.html')

@app.route('/api/menu')
def get_menu():
    category = request.args.get('category', None)
    
    if category:
        menu_items = MenuItem.query.filter_by(category=category).filter_by(is_available=True).all()
    else:
        menu_items = MenuItem.query.filter_by(is_available=True).all()
    
    return jsonify([item.to_dict() for item in menu_items])

@app.route('/api/menu/featured')
def get_featured_menu():
    featured_items = MenuItem.query.filter_by(featured=True).filter_by(is_available=True).all()
    return jsonify([item.to_dict() for item in featured_items])

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    try:
        data = request.json
        
        # Create reservation object
        reservation = Reservation(
            full_name=data['fullName'],
            email=data['email'],
            phone=data['contactNumber'],
            date=datetime.datetime.strptime(data['reservationDate'], '%Y-%m-%d').date(),
            time=data['reservationTime'],
            guests=int(data['guestCount']),
            seating_type=data['seatingType'],
            special_requests=data.get('specialRequests', '')
        )
        
        db.session.add(reservation)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Reservation created successfully!',
            'reservation_id': reservation.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error creating reservation: {str(e)}'
        }), 400

@app.route('/api/contact', methods=['POST'])
def create_contact_message():
    try:
        data = request.json
        
        # Create contact message object
        message = ContactMessage(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', None),
            message=data['message']
        )
        
        db.session.add(message)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully!',
            'message_id': message.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error sending message: {str(e)}'
        }), 400

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)