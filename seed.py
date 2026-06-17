from app import create_app, db
from app.model import User, Role
from app.employee.model import Employee
from datetime import datetime

def seed():
    app = create_app()
    with app.app_context():
        # 1. Create Tables
        db.create_all()

        # 2. Add Roles
        admin_role = Role.query.filter_by(name='Admin').first()
        if not admin_role:
            admin_role = Role(name='Admin')
            db.session.add(admin_role)
        
        employee_role = Role.query.filter_by(name='Employee').first()
        if not employee_role:
            employee_role = Role(name='Employee')
            db.session.add(employee_role)
        
        db.session.commit()

        # 3. Add Admin: Mukarram
        mukarram = User.query.filter_by(username='mukarram').first()
        if not mukarram:
            mukarram = User(username='mukarram')
            mukarram.set_password('admin123') # Default password
            mukarram.roles.append(admin_role)
            db.session.add(mukarram)
            print("Added admin: mukarram")
        else:
            print("Admin mukarram already exists")

        # 4. Add Employees
        employees_to_add = [
            {'name': 'Muskan', 'fathername': 'Unknown'},
            {'name': 'Hamza Amjad', 'fathername': 'Unknown'}
        ]

        for emp_data in employees_to_add:
            emp = Employee.query.filter_by(name=emp_data['name']).first()
            if not emp:
                new_emp = Employee(
                    name=emp_data['name'],
                    fathername=emp_data['fathername'],
                    dob=datetime(1995, 1, 1), # Placeholder DOB
                )
                db.session.add(new_emp)
                print(f"Added employee: {emp_data['name']}")
            else:
                print(f"Employee {emp_data['name']} already exists")

        db.session.commit()
        print("Seeding completed successfully!")

if __name__ == '__main__':
    seed()
