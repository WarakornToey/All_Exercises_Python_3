import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-9bd58-firebase-adminsdk-rpvy5-3ae9ba7b50.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-9bd58-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')

posts_ref = ref.child('Users')
new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})

hopper_ref = ref.child('Users/Somsong')
hopper_ref.delete() #จะ Update .update

print(ref.get())