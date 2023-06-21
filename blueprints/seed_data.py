from datetime import date
from time import time

from models.user import User
from models.album import Album
from models.track import Track
from models.musician import Musician
# from models.track_musician import Track_Musician
from utilities import generate_pw

users = [
    User(
    name = "Personnel Dev",
    email = "dev@cs.com",
    password = generate_pw('dev'),
    is_admin = True,
    date_created = date.today(),
    last_updated = date.today()
    ),
    User(
    name = "Julian Adderly",
    email = "alto@cannonball.com",
    password = generate_pw('soul'),
    is_admin = False,
    date_created = date.today(),
    last_updated = date.today()
    )
]



albums = [
    Album(
    title = "Water Babies",
    artist = "Miles Davis",
    release_date = "11/2/1976",
    genre = "Post Bop",
    img_url = "https://i.discogs.com/ws-wRUxz6wzx0-CYDo7tu8JN_5yQE-j-1JRayeO0zr8/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTY2ODQ2/LTEyMDkxNjgxNzUu/anBlZw.jpeg",
    # created_by = 0,
    label = "Columbia",
    date_created = date.today(),
    last_updated = date.today()
    ),
    Album(
    title = "Aja",
    artist = "Steely Dan",
    release_date = "9/23/1977",
    genre = "Rock/Fusion",
    img_url = "https://i.discogs.com/3Pxzvua2yABfdbcOVeiTdXiLvIYxULvquQzSG6Cj-ak/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE4NDIz/MzQtMTMxOTU5NTc4/NC5qcGVn.jpeg",
    # created_by = 0,
    label = "ABC",
    date_created = date.today(),
    last_updated = date.today()
    ),
    Album(
    title = "Future Shock",
    artist = "Herbie Hancock",
    release_date = "7/1/1983",
    label = "Columbia",
    genre = "Fusion",
    img_url = "https://upload.wikimedia.org/wikipedia/en/e/eb/Herbie_Hancock_-_Rockit.jpg",
    # created_by = 0,
    date_created = date.today(),
    last_updated = date.today()
    ),
    Album(
    title = "Red Clay",
    artist = "Freddie Hubbard",
    release_date = "5/1/1970",
    label = "CTI",
    genre = "Fusion",
    img_url = "",
    # created_by = 0,
    date_created = date.today(),
    last_updated = date.today()
    )
]


water_babies = Track(
        album_id = 1,
        title = 'Water Babies',
        track_number = 1,
        duration = '05:08',
        date_created = date.today(),
        last_updated = date.today()
    ),
capricorn = Track(
        album_id = 1,
        title = 'Capricorn',
        track_number = 2,
        duration = '08:29',
        date_created = date.today(),
        last_updated = date.today()

    ),
sweet_pea = Track(
        album_id = 1,
        title = 'Sweet Pea',
        track_number = 3,
        duration = '08:02',
        date_created = date.today(),
        last_updated = date.today()
    ),
two_faced = Track(
        album_id = 1,
        title = 'Two Faced',
        track_number = 4,
        duration = '18:02',
        date_created = date.today(),
        last_updated = date.today()
    ),
dual = Track(
        album_id = 1,
        title = 'Dual Mr. Anthony Tillmon Williams Process',
        track_number = 5,
        duration = '13:22',
        date_created = date.today(),
        last_updated = date.today()
    ),
splash = Track(
        album_id = 1,
        title = 'Splash',
        track_number = 6,
        duration = '10:05',
        date_created = date.today(),
        last_updated = date.today()
    ),


tracks = [water_babies, capricorn, sweet_pea, two_faced, dual, splash]


musicians = [
    Musician(
        f_name = 'Miles',
        l_name = 'Davis',
        instrument = 'Trumpet',
        birthdate = '05/26/1926',
        expiry = '9/28/1991',
        img_url = 'https://2.bp.blogspot.com/_5VxK1gkg1U4/TVLCM0z5VdI/AAAAAAAAAU8/IbTXIR-ZiqA/s1600/milesdavis.jpg',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Wayne',
        l_name = 'Shorter',
        instrument = 'Saxophone',
        birthdate = '8/25/1933',
        expiry = '3/2/2023',
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Herbie',
        l_name = 'Hancock',
        instrument = 'Piano, Fender Rhodes',
        birthdate = '04/12/1940',
        
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Ron',
        l_name = 'Carter',
        instrument = 'Bass',
        birthdate = '05/4/1937',
        
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Tony',
        l_name = 'Williams',
        instrument = 'Drums',
        birthdate = '12/12/1945',
        expiry = '2/23/1997',
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Chick',
        l_name = 'Corea',
        instrument = 'Piano, Fender Rhodes',
        birthdate = '6/12/1941',
        expiry = '2/9/2021',
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Dave',
        l_name = 'Holland',
        instrument = 'Bass',
        birthdate = '10/1/1946',
        
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    ),
    Musician(
        f_name = 'Jack',
        l_name = 'DeJohnette',
        instrument = 'Drums',
        birthdate = '8/9/1942',
        
        img_url = '',
        date_created = date.today(),
        date_updated = date.today()
    )
]

# track_musicians = [
#     # TRACK 1
#     Track_Musician(
#         track_id = 1,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 1,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 1,
#         musician_id = 3,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 1,
#         musician_id = 4,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 1,
#         musician_id = 5,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),

#     # TRACK 2
#     Track_Musician(
#         track_id = 2,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 2,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 2,
#         musician_id = 3,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 2,
#         musician_id = 4,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 2,
#         musician_id = 5,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 2,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),

#     # TRACK 3
#     Track_Musician(
#         track_id = 3,
#         musician_id = 4,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 3,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 3,
#         musician_id = 3,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 3,
#         musician_id = 4,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 3,
#         musician_id = 5,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),

#     # TRACK 4
#     Track_Musician(
#         track_id = 4,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 4,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 4,
#         musician_id = 6,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 4,
#         musician_id = 7,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 4,
#         musician_id = 8,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),

#     # TRACK 5
#     Track_Musician(
#         track_id = 5,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 5,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 5,
#         musician_id = 6,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 5,
#         musician_id = 7,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 5,
#         musician_id = 8,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),

#     # TRACK 6
#         Track_Musician(
#         track_id = 6,
#         musician_id = 1,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 6,
#         musician_id = 2,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 6,
#         musician_id = 6,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 6,
#         musician_id = 7,
#         date_created = date.today(),
#         date_updated = date.today()
#     ),
#     Track_Musician(
#         track_id = 6,
#         musician_id = 8,
#         date_created = date.today(),
#         date_updated = date.today()
#     )
# ]


