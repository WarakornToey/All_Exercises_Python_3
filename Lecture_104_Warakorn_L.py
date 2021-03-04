class Customer: #คือพิมพ์เขียว หรือ รูปแบบโครงสร้าง ว่าโครงสร้างมีอะไรบ้าง
    name = ""
    lastName = ""
    age = 0

    def  addCart(self): #ประกาศฟังก์ชันเพื่อเรียกใช้งาน
        print("Add Product to ",self.name,self.lastName,self.age,"'s cart")

customer1 = Customer() #customer1 ประกาศตัวเเปรเพื่อเก็บข้อมูล Class หรือเรียกว่าการสร้าง Object หรือวัตถุ 1 ตัว
customer1.name = "Warakorn"
customer1.lastName = "Laoprom"
customer1.age = 28
customer1.addCart() #เรียกใช้งาน Class

customer2 = Customer()
customer2.name = "Ruckchanok"
customer2.lastName = "Chaiyarak"
customer2.age = 29
customer2.addCart()

customer3 = Customer()
customer3.name = "Tor"
customer3.lastName = "Toey"
customer3.age = 30
customer3.addCart()

customer4 = Customer()
customer4.name = "Som"
customer4.lastName = "LiLi"
customer4.age = 20
customer4.addCart()