import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zooweb.settings')

import django

django.setup()
from rango.models import AnimalCategory, Animal


def populate():


    Birds = [
        {
            'animal_name': 'Black Stork',
            'category': 'Birds',
            "size":"Adult birds have a body length of 1-1.2 meters and a weight of 2-3 kilograms.",
            'distribution_area': 'Afghanistan, Albania, Algeria, Angola, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bhutan, Bosnia and Herzegovina, Botswana, Bulgaria, Central African Republic, China, Ivory Coast, Croatia, Cyprus, Czech Republic, Denmark',
            'likes': 56,
            'brief':"Black stork (scientific name: Ciconia nigra) is a large wading bird with a graceful posture, bright body color, agile movement and alert temperament. The mouth is long and sturdy, the head, neck, and feet are very long, and the mouth and feet are red. Except for the pure white chest and abdomen, the feathers on the body are all black. Under different angles of light, they can reflect a variety of colors. Build large nests on tall trees or rocks, with your head and neck straight when flying.",
            'picture': 'animals_images/blackstork.jpg'
        },
        {
            'animal_name': 'Chilean Flamingo',
            'category': 'Birds',
            'size': 'The weight is 2500-3500 grams, the body length is 79-145 cm, and the wingspan is 127-153 cm. The mouth is short and thick, the middle of the upper mouth is protruding downwards, and the lower mouth is larger and groove-shaped; the neck is long and curved; the feet are extremely long and bare, with webs between the forward 3 toes, and the hind toes are short and do not touch the ground; the size of the wings is moderate ; Tail is short; body feathers are white and rosy, flying feathers are black, and cover feathers are dark red',
            'distribution_area': 'Argentina, Bolivia, Brazil, Chile, Ecuador, Paraguay, Peru, Uruguay',
            'likes': 89,
            "brief":"Chilean Flamingo (scientific name: Phoenicopterus chilensis) is a water bird with pinkish plumage. The mouth is pink and black, the mouth is shaped like a boot, the neck is long, the legs are red, and the wings are reddish. Sub-adults are light brown with gray beak.",
            'picture': 'animals_images/chileanflamingo.jpg'
        },
        {
            'animal_name': 'Egyptian Vulture',
            'category': 'Birds',
            "size":"The body length is 58-70 cm, the wingspan is 155-170 cm, and the weight is 1.6-2.2 kg.",
            'distribution_area': 'Afghanistan, Albania, Algeria, Andorra, Angola, Armenia, Azerbaijan, Benin, Bulgaria, Burkina Faso, Cameroon, Cape Verde, Central African Republic, Chad, Cyprus, Djibouti, Egypt, Eritrea, Ethiopia, France, Ghana',
            'likes': 55,
            'brief': "Known as Pharaoh’s chicken, this species is called the scavenger vulture in South Asia. Adult birds mostly have white to light gray feathers, which contrast sharply with the black wing and tail feathers and bare yellow skin. Has a shawl-shaped mane. The long and narrow beak has a yellow base, a black tip, and very pointed wings. Among them, the third main feather is the longest. The tail is short and wedge-shaped. The legs are off-white, pink or light yellow. The feathers of the chicks are much darker than that of the adult birds, and are gray-brown, brown, or black-brown, with black and white spots.",
            'picture': 'animals_images/egyptian_vulture.jpg'
        },
        {
            'animal_name': 'Southern Cassowary',
            'category': 'Birds',
            'size':"It is tall, weighing 29-59 kg, and having a body length of 102-170 cm. The largest cassowary is 150 cm tall.",
            "distribution_area":"Australia, Indonesia and Papua New Guinea",
            'likes': 61,
            'brief': "Double-falling cassowary (scientific name: Casuarius casuarius) is a bird of the Ornithidae and Struthioidae, also known as 'double-falling cassowary.' Protective horny helmet on top of the head. It can hit the grass when walking through the forest. Their wings degenerate earlier than those of the ostrich and rheas, and cannot fly. The head is blue, with one or two red lapels in the throat, black feathers, long legs, strong and powerful, with sharp claws. Three toes, of which the inner toe has a long and sharp claw for defense.",
            'picture': 'animals_images/cassowary.jpg'
        },
    ]

    Mammals = [
        {
            "animal_name": "Binturong",
            "category": "Mammals",
            "size": "Binturong weighs 8 to 13 kg, has a body length of 700 to 800 mm, and has a stout tail that is about the same length as its body. Its body hair is black with light brownish-yellow mixed with brownish-yellow or brownish-gray hair tips, and the tail color is similar to the back color.",
            "distribution_area": "Nepal, Sikkim, Bhutan, India (Assam), Myanmar, Thailand, Laos, Vietnam, Cambodia, Malaysia, Indonesia and the Philippines. The largest subspecies peninsula subspecies is distributed in the Philippines.",
            "likes": 99,
            "brief": "Binturong (scientific name: Arctictis binturong), also known as bear civet, is the second largest species in the civet family. Its body hair is black and fluffy, mixed with light brown-yellow. The tufts on the ear tip are as long as 5 cm, and the ear edge is white. The limbs are strong, with five toes long and claws; the tail has a winding function different from other animals in the same family. The head, eye area, forehead and chin are dark gray, and the long beards around the lips are white",
            "picture": "animals_images/binturong.jpg"
        },
        {
            "animal_name": "Chimpanzee",
            "category": "Mammals",
            "size": "Chimpanzees are very similar in shape to gorillas. Because of their thicker body hair, they also look thinner. Males are 110-140 cm in length, 1-1.7 meters tall when standing, and weigh 50-75 kg. Females are smaller than males. , But the difference between males and females is not as great as that of gorillas.",
            "distribution_area": "Angola, Burundi, Cameroon, Central African Republic, Congo, Democratic Republic of Congo, Côte d’Ivoire, Equatorial Guinea, Gabon, Ghana, Guinea, Guinea-Bissau, Liberia, Mali, Nigeria, Rwanda, Senegal, Sierra Leone, South Sudan, United Republic of Tanzania , Uganda",
            "likes": 91,
            "brief": "The body coat is short, black, usually with white spots on the buttocks, gray-brown face, gray hands and feet covered with sparse black hair; the nose, ears, hands and feet of the baby chimpanzee are all flesh-colored The ears are very large, protruding to the sides, the eye sockets are deep, the eyebrows are high, and the hair on the top of the head is backward; the hands are 24 cm long; the canine teeth are developed, and the teeth are the same as those of humans; there is no tail.",
            "picture": "animals_images/chimpanzee.jpg"
        },
        {
            "animal_name": "Giant Panda",
            "category": "Mammals",
            "size": "The giant panda is fat like a bear, plump and rich, with a round head and a short tail, with a head and body length of 1.2-1.8 meters and a tail length of 10-12 cm. The weight is 80-120 kg, and the maximum weight can reach 180 kg. The pandas raised are slightly heavier, and the males are generally slightly larger than the females.",
            "distribution_area": "China (Sichuan, Shaanxi and Gansu)",
            "likes": 999,
            "brief": "Giant panda (scientific name: Ailuropoda melanoleuca);The only mammal belonging to the genus Carnivora, Ursidae, Giant Panda subfamily and Giant Panda. There are only two subspecies. The body color is black and white, the cheeks are round, there are large dark circles, the iconic inner figure walking style, and the sharp claws like a scalpel. The giant panda's skin is thick, up to 10 mm at its thickest point. The black and white appearance is conducive to hiding in dense forest trees and snow-covered ground without being easily spotted by natural enemies.",
            "picture": "animals_images/giant_panda.jpg"
        },
        {
            "animal_name": "Koala",
            "category": "Mammals",
            "size": "The adult koala is about 70-80 cm long and weighs about 10 kg. The body is light gray to light yellow.",
            "distribution_area": "Australia (New South Wales, Queensland, South Australia, Victoria)",
            "likes": 89,
            "brief": "Koala (scientific name: Phascolarctos cinereus) is an animal of the Koala family and Koala genus. It has a fat body, messy and thick hair, and no tail. Adult koalas are light gray to light yellow. The color around the abdomen is relatively bright. The nose is bald, large and round, and the head is round. The hair on the ears is very fluffy. The forelimbs have very strong claws and are good at climbing. Male koalas weigh 50% more than females, have a relatively wide face, a pair of relatively small ears, and a relatively large odor-emitting thymus. The main secondary sex characteristic of females is their baby pouch, which has 2 teats inside and opens towards the rear end.",
            "picture": "animals_images/koala_goonaroo.jpg"
        },
        {
            "animal_name": "Nubian giraffes",
            "category": "Mammals",
            "size": "The named subspecies of giraffes are 380-470 cm long. Both males and females have a pair of small short horns covering the skin and hair on the tops of their heads. The background color is light brown and will not take off for life.",
            "distribution_area": "Nubia, eastern Sudan, South Sudan, and northeastern Democratic Republic of Congo",
            "likes": 70,
            "brief": "The color of the giraffe fur has spots and patterns. The head has a wide forehead, a sharp snout, large ears, and a pair of short bony horns on the top of the head. The horns cover the skin and hair; the neck is particularly long (about 2 meters). ), with 1 row of bristles on the nape; short body; high and strong limbs, forelimbs slightly longer than hind limbs, broad hoof; short tail with black tufts at the end. The teeth are primitive low-crown teeth, which cannot feed on grass as the staple food, but only on leaves; the tongue is longer and can be used for feeding; it has short horns, and the horns are covered by hairy skin. Living in the savanna area of Africa, it is a herbivore and feeds mainly on leaves and twigs.",
            "picture": "animals_images/giraffes.jpg"
        }
    ]

    Amphibians = [
        {
            "animal_name": "Blue Poison Arrow Frog",
            "category": "Amphibians",
            "size": "Its body length is between 3 and 4 cm, and its life span can reach 5 years.",
            "distribution_area": "Central and South America are concentrated in Suriname in the tropical rain forest area close to the equator.",
            "likes": 33,
            "brief": "The blue poison dart frog is also called the blue poison dart frog. This petite, beautiful and sometimes life-threatening amphibian was not known to scientists until a few specimens were brought back from the Amazon in 1968. This poison frog is one of the animals used by the natives of South America. These animals have deadly toxins hidden under their brilliant blue skin.",
            "picture": "animals_images/bluepoisondartfrogs.jpg"
        },
        {
            "animal_name": "Phantasmal Poison Arrow Frog",
            "category": "Amphibians",
            "size": "The phantasmal poison frog has a snout-to-vent length of about 22.6 mm (0.9 in). It has a wide head and truncated snout and the skin is smooth. The first finger is longer than the second, and all the digits are partially webbed. The dorsal surface is usually green or yellow and there are longitudinal stripes",
            "distribution_area": "The phantasmal poison frog is known only from a number of locations in central Ecuador on the Andean slopes of Bolívar Province, at heights of between 319 and 1,769 m (1,047 and 5,804 ft) above sea level. Its natural habitat is the leaf litter on the floor of the tropical forest, especially near streams, and in wetlands",
            "likes": 10,
            "brief": "The phantasmal poison frog or phantasmal poison-arrow frog (Epipedobates tricolor) is a species of poison dart frog. It is endemic to Ecuador and known from the Andean slopes of central Ecuador in Bolívar Province. They have radiant colors. This species is endangered, and there are only a few locations in the wild where they are known to live.",
            "picture": "animals_images/phantasmalpoisonarrowfrog.jpg"
        },
    ]

    Reptiles = [
        {
            "animal_name": "Pancake tortoise",
            "category": "Reptiles",
            "size": "The pancake tortoise has an unusually thin, flat, flexible shell, which is up to 17.8 centimetres (7.0 in) long",
            "distribution_area": "n East African species, M. thornier is native to southern Kenya and northern and eastern Tanzania, and an introduced population may also occur in Zimbabwe.",
            "likes": 31,
            "brief": "The pancake tortoise (Malacochersus tornieri) is a species of flat-shelled tortoise in the family Testudinidae. The species is native to Tanzania and Kenya. Its common name refers to the flat shape of its shell.",
            "picture": "animals_images/pancaketortoise.jpg"
        },
        {
            "animal_name": "Alligator",
            "category": "Reptiles",
            "size": "An average adult American alligator's weight and length is 360 kg (790 lb) and 4 m (13 ft), but they sometimes grow to 4.4 m (14 ft) long and weigh over 450 kg (990 lb).The largest ever recorded, found in Louisiana, measured 5.84 m (19.2 ft).The Chinese alligator is smaller, rarely exceeding 2.1 m (7 ft) in length. Additionally, it weighs considerably less, with males rarely over 45 kg (100 lb)",
            "distribution_area": "China,America",
            "likes": 95,
            "brief": "An alligator is a crocodilian in the genus Alligator of the family Alligatoridae. The two extant species are the American alligator (A. mississippiensis) and the Chinese alligator (A. sinensis). Additionally, several extinct species of alligator are known from fossil remains. Alligators first appeared during the Oligocene epoch about 37 million years ago.",
            "picture": "animals_images/Alligator.jpg"
        },
        {
            "animal_name": "Dendroaspis polylepis",
            "category": "Reptiles",
            "size": "The black mamba is a long, slender, cylindrical snake. It has a coffin-shaped head with a somewhat pronounced brow ridge and a medium-sized eye.The adult snake's length typically ranges from 2 to 3 m (6 ft 7 in to 9 ft 10 in) but specimens have grown to lengths of 4.3 to 4.5 m (14 ft 1 in to 14 ft 9 in).The body mass of black mambas has been reported to be about 1.6 kg (3.5 lb),although a study of seven black mambas found an average weight of 1.03 kg (2.3 lb).",
            "distribution_area": "The black mamba inhabits a wide range in sub-Saharan Africa; its range includes Burkina Faso, Cameroon, Central African Republic, Democratic Republic of the Congo, South Sudan, Ethiopia, Eritrea, Somalia, Kenya, Uganda, Tanzania, Burundi, Rwanda, Mozambique, Swaziland, Malawi, Zambia, Zimbabwe, Botswana, South Africa, Namibia, and Angola",
            "likes": 29,
            "brief": "The black mamba (scientific name: Dendroaspis polylepis) is a large venomous snake distributed in sub-Saharan Africa. Its body color is gray or brown, its larvae are lighter, and its color gradually darkens with age.",
            "picture": "animals_images/Dendroaspis_polylepis.jpg"
        },
        {
            "animal_name": "Green sea turtle",
            "category": "Reptiles",
            "size": "Generally speaking, wild green turtles take 20-50 years to mature. Mature green turtles are about 90 to 135 cm long and weigh more than 100 kg.",
            "distribution_area": "Green tortoises are widely distributed in tropical and subtropical waters, that is, the waters between the 20°C isotherm at north-south latitude",
            "likes": 59,
            "brief": "Green sea turtle (scientific name: Chelonia mydas, English: green sea turtle), also known as green sea turtle, is a reptile in the ocean and the only species in the genus of sea turtles. I spent most of my life living in the sea, but part of the ancestor’s way of life was still retained in the evolution process, so I had to return to the place of birth to lay eggs and breed offspring, forming a more unique life habit.",
            "picture": "animals_images/greenspottedpufferfish.jpg"
        },
    ]

    Fish = [
        {
            "animal_name": "Banded Archer Fish",
            "category": "Fish",
            "size": "Larger specimens may be able to hit prey 2 to 3 metres (6 ft 7 in to 9 ft 10 in) away.[4] The banded archerfish may reach the displaced prey within 50 milliseconds of its hitting the water",
            "distribution_area": "The banded archerfish inhabits the Indo-Pacific and waters off northern Australia, and less frequently those on the southern coast of Australia.",
            "likes": 42,
            "brief": "The banded archerfish (Toxotes jaculatrix) is a brackish water perciform fish of the archerfish genus Toxotes. It is silvery in colour and has a dorsal fin towards the posterior end. It has distinctive, semi-triangular markings along its sides. It is best known for its ability to spit a jet of water to 'shoot down' prey.",
            "picture": "animals_images/bandedarcherfish.jpg"
        },
        {
            "animal_name": "Green spotted pufferfish",
            "category": "Fish",
            "size": "Adult fish can grow up to about 15-20 cm. The whole body is about a horizontal ellipse, the skin above the fins (including the back) is golden yellow, and there are black round spots interlaced among them, similar to leopard prints",
            "distribution_area": "Watersheds in Thailand, Cambodia, Malaysia, Myanmar, China",
            "likes": 88,
            "brief": "The black puffer puffer, also known as the dark green puffer and the golden doll, is one of the four-dented pufferfish in the suborder Tetradente of the radiating finfish. It lives in fresh or brackish water offshore. Heiqingbanhe River Pufferfish are quite common in aquariums in Shanghai and Taiwan and are often referred to as 'golden dolls'. Generally, the best breeding temperature is about 24~27℃, and the bottom sand is preferably alkaline coral sand. Generally, 2% sea salt is added to the water.",
            "picture": "animals_images/greenspottedpufferfish.jpg"
        },
        {
            "animal_name": "Amphiprioninae",
            "category": "Fish",
            "size": "The largest can reach a length of 17 cm (6.7 in), while the smallest barely achieve 7–8 cm (2.8–3.1 in).",
            "distribution_area": "Anemonefish are endemic to the warmer waters of the Indian Ocean, including the Red Sea and Pacific Oceans, the Great Barrier Reef, Southeast Asia, Japan, and the Indo-Malaysian region. ",
            "likes": 200,
            "brief": "Clownfish or anemonefish are fishes from the subfamily Amphiprioninae in the family Pomacentridae. Thirty species are recognized: one in the genus Premnas, while the remaining are in the genus Amphiprion. In the wild, they all form symbiotic mutualisms with sea anemones. Depending on species, anemonefish are overall yellow, orange, or a reddish or blackish color, and many show white bars or patches. ",
            "picture": "animals_images/Amphiprion.jpg"
        }
    ]


    cats={
        'Birds':{'animal':Birds,'views':121},
        'Mammals': {'animal': Mammals, 'views': 233},
        'Amphibians': {'animal': Amphibians, 'views': 88},
        'Reptiles': {'animal': Reptiles, 'views': 228},
        'Fish': {'animal': Fish, 'views': 99}
    }


    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'])
        for animal in cat_data['animal']:
            add_aniaml(cat=c, animal_name =animal['animal_name'],size=animal['size'],distribution_area=animal["distribution_area"],
                       brief=animal['brief'],pictrue=animal['picture'],likes=animal['likes'])


    for c in AnimalCategory.objects.all():
        for animal in Animal.objects.filter(category=c):
            print(f'- {c}: {animal}')

def add_aniaml(cat,animal_name, size,distribution_area, brief, pictrue,likes=0):
    a = Animal.objects.get_or_create(category=cat, animal_name=animal_name)[0]
    a.size = size
    a.distribution_area = distribution_area
    a.likes = likes
    a.brief = brief
    a.picture = pictrue

    a.save()
    return a


def add_cat(name, views=0):
    c = AnimalCategory.objects.get_or_create(category_name=name)[0]
    c.views = views
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting population script...')
    populate()
