from app import app, db, MenuItem
import datetime

# Use the application context
with app.app_context():
    # Check if menu items already exist
    if MenuItem.query.count() == 0:
        # Sample menu items
        menu_items = [
            # Appetizers
            MenuItem(
                name="Samosas",
                description="Crispy pastry filled with spiced potatoes and peas, served with mint chutney",
                price=120,
                category="appetizers",
                image_url="https://images.unsplash.com/photo-1601050690597-df0568f70950?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=True
            ),
            MenuItem(
                name="Vegetable Pakoras",
                description="Seasonal vegetables dipped in spiced chickpea batter and deep-fried to perfection",
                price=150,
                category="appetizers",
                image_url="https://images.unsplash.com/photo-1630910395218-9d2e4c0a6e2c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            ),
            MenuItem(
                name="Dahi Puri Chaat",
                description="Crisp puris filled with potatoes, chickpeas, yogurt and tangy tamarind chutney",
                price=180,
                category="appetizers",
                image_url="https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            ),
            
            # Main Courses
            MenuItem(
                name="Chicken Biryani",
                description="Fragrant basmati rice cooked with tender chicken and authentic biryani spices",
                price=450,
                category="mains",
                image_url="https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2088&q=80",
                is_available=True,
                featured=True
            ),
            MenuItem(
                name="Beef Nihari",
                description="Slow-cooked beef shank in a rich, spicy gravy, served with naan",
                price=550,
                category="mains",
                image_url="https://images.unsplash.com/photo-1603360946369-dc9bb6258143?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            ),
            MenuItem(
                name="Chicken Karahi",
                description="Traditional wok-cooked chicken with tomatoes, ginger, and green chilies",
                price=650,
                category="mains",
                image_url="https://images.unsplash.com/photo-1601050690117-94b5b7e50a33?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            ),
            
            # BBQ Specials
            MenuItem(
                name="Seekh Kebabs",
                description="Minced beef skewers with traditional spices, grilled over charcoal",
                price=350,
                category="bbq",
                image_url="https://images.unsplash.com/photo-1603360946369-dc9bb6258143?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            ),
            MenuItem(
                name="Chicken Tikka",
                description="Succulent chicken pieces marinated in yogurt and spices, grilled to perfection",
                price=380,
                category="bbq",
                image_url="https://images.unsplash.com/photo-1601050690117-94b5b7e50a33?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=True
            ),
            
            # Desserts
            MenuItem(
                name="Gulab Jamun",
                description="Soft milk solids dumplings, soaked in rose-scented syrup",
                price=180,
                category="desserts",
                image_url="https://images.unsplash.com/photo-1565557623262-b51c2513a641?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80",
                is_available=True,
                featured=False
            ),
            MenuItem(
                name="Kheer",
                description="Creamy rice pudding with cardamom, saffron, and topped with nuts",
                price=200,
                category="desserts",
                image_url="https://images.unsplash.com/photo-1574711859537-b906e1fb4f89?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
                is_available=True,
                featured=False
            )
        ]
        
        # Add menu items to database
        for item in menu_items:
            db.session.add(item)
        
        # Commit changes
        db.session.commit()
        
        print("Database seeded successfully!")
    else:
        print("Menu items already exist. Database seeding skipped.")