from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__, template_folder=r"C:\Users\MALA\Desktop\codsoft")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/savedetails", methods=["POST"])
def saveDetails():
    msg = ""
    if request.method == "POST":
        try:
            name = request.form["name"]
            phone_no = request.form["phone_no"]
            email = request.form["email"]
            address = request.form["address"]
            with sqlite3.connect("contact.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO contactdetails (name, phone_no, email, address) VALUES (?, ?, ?, ?)",
                            (name, phone_no, email, address))
                con.commit()
                msg = "Contact successfully added"
        except Exception as e:
            con.rollback()
            msg = "Failed to add contact: " + str(e)
        finally:
            con.close()
            return render_template("success.html", msg=msg)

@app.route("/view")
def view():
    con = sqlite3.connect("contact.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM contactdetails")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

class AddressBook:
    @staticmethod
    def search_contact(name):
        try:
            with sqlite3.connect("contact.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM contactdetails WHERE name LIKE ?", ('%' + name + '%',))
                contacts = cursor.fetchall()
                return contacts
        except sqlite3.Error as e:
            print("Error searching contacts:", e)
            return []

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        address_book = AddressBook()
        search_name = request.form['search_name']
        search_results = address_book.search_contact(search_name)
        return render_template('search_results.html', results=search_results)
    return render_template('search.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_contact(id):
    if request.method == "POST":
        try:
            name = request.form["name"]
            phone = request.form["phone"]
            email = request.form["email"]
            address = request.form["address"]
            
            with sqlite3.connect("contact.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE contactdetails SET name=?, phone=?, email=?, address=? WHERE id=?", (name, phone, email, address, id))
                conn.commit()
            
            return redirect("/")
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        try:
            with sqlite3.connect("contact.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM contactdetails WHERE id=?", (id,))
                contact = cursor.fetchone()
                
            if contact:
                return render_template("edit_contact.html", contact=contact)
            else:
                return "Contact not found"
        except Exception as e:
            return f"An error occurred: {str(e)}"
@app.route("/delete")
def delete():
    return render_template("Delete.html")
@app.route("/deleterecord", methods=["GET", "POST"])
def deleterec():
    if request.method == "POST":
        try:
            id = request.form["id"]
            with sqlite3.connect("contact.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM contactdetails WHERE id = ?", (id,))
                con.commit()
                msg = "Contact successfully deleted"
        except Exception as e:
            msg = "Can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)
    return render_template("Delete.html")

if __name__ == "__main__":
    app.run(debug=True)
