
import streamlit as st
from streamlit_lottie import st_lottie
from gtts import gTTS
import random
import os

# Set page config
st.set_page_config(page_title="Kids Learning App", layout="centered")
st.title("🎵 Kids Learning 🌟")
st.markdown("### 🎶 Enjoy fun animations, relaxing music, soothing voice & moral stories!")

# --- 🎨 Lottie Animation ---
lottie_animation = "https://assets2.lottiefiles.com/packages/lf20_u4yrau.json"
st_lottie(lottie_animation, height=300, key="lottie")

# --- 🎼 Relaxing Background Music ---
st.markdown("### 🎼 Choose a Relaxing Music")

audio_tracks = {
    "🌿 Calm Piano": "balance-piano-music-297441.mp3",
    "🌊 Ocean Waves": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "🎸 Soft Guitar": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "🛶 River Flow": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "🌅 Morning Breeze": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
}

selected_audio = st.selectbox("🎼 Choose your background music:", list(audio_tracks.keys()))
if st.button("▶ Play Music"):
    st.audio(audio_tracks[selected_audio], format="audio/mp3")

# --- 📖 Moral Story Section ---
st.markdown("---")
st.markdown("## 📖 *Today's Moral Story*")

stories = [
    {
        "title": "The Honest Woodcutter 🪓",
        "content": "A poor woodcutter was cutting trees near a river when his axe slipped from his hands and fell into the water. He sat down sadly, wondering how he would continue his work. Suddenly, a fairy appeared and asked what had happened. After hearing his story, she dived into the water and returned with a golden axe. The woodcutter shook his head and said, 'This is not mine.' She then returned with a silver axe, and again he refused. Finally, she brought back his old iron axe. The woodcutter was overjoyed and thanked her. Seeing his honesty, the fairy gifted him all three axes.",
        "moral": "Honesty is the best policy."
    },
    {
        "title": "The Lion & The Mouse 🦁🐭",
        "content": "One day, a mighty lion was taking a nap when a little mouse started running up and down on his body. This woke up the lion, and he grabbed the mouse angrily. 'How dare you disturb me!' he roared. The mouse pleaded for mercy and promised to help him someday. The lion laughed and let him go. Days later, the lion was caught in a hunter's net. He roared for help, and the little mouse quickly came and gnawed the ropes, setting him free. The lion realized that kindness is never wasted.",
        "moral": "A kind act is never wasted."
    },
    {
        "title": "The Boy Who Cried Wolf 🐺",
        "content": "A shepherd boy was bored while watching his flock. To entertain himself, he cried out, 'Wolf! Wolf!' The villagers came running to help, only to find the boy laughing. He repeated this trick multiple times, and the villagers stopped believing him. One day, a real wolf came. The boy screamed for help, but no one came. The wolf attacked the flock, and the boy learned a painful lesson.",
        "moral": "Lying breaks trust and leads to consequences."
    },
    {
  "title": "The Kind Little Cloud ☁️",
  "content": "A little white cloud went floating one day,\nAcross the bright sky in a cheerful way.\nShe danced with the breeze, soft and light,\nPlaying peek-a-boo with the golden sunlight.\n\nBelow her lay fields, dry and brown,\nThe flowers all drooped, their heads hanging down.\nThe trees looked tired, the grass had gone pale,\nNo laughter of wind, no splash from the hail.\n\nThe little cloud frowned and gave a small sigh,\n“I must do something,” she said to the sky.\nSo she puffed up her cheeks and turned a bit grey,\nThen rumbled a song in a thunderous way.\n\nShe sprinkled down raindrops in gentle delight,\nTickling leaves, making streams sparkle bright.\nThe lilies stood tall, the roses gave cheer,\nEven the bees gave a thankful cheer!\n\nThe rainbow arrived like a magical smile,\nStretching across the sky for a while.\nThe sun gave a wink, the wind clapped aloud,\nAll cheered for the kind little cloud.\n\nThen off she floated, soft as a sigh,\nWhistling tunes to the birds flying by.\nShe left behind laughter, green hills, and cheer,\nPromising always to be somewhere near.",
  "moral": "Small acts of kindness can make a big difference."
},
{
  "title": "Tommy the Turtle 🐢",
  "content": "Tommy the turtle, quiet and shy,\nMoved so slow, you’d think he might fly—\nBackwards! they joked, each animal friend,\nBut Tommy believed he'd win in the end.\n\nThe rabbits would race, the squirrels would spin,\nThe frogs would leap with a cheeky grin.\nTommy just smiled and stayed on his track,\nNever once thinking of turning back.\n\nOne day the animals set up a race,\nTo test their skills and show off their pace.\nThe rabbit was sure he’d win in a flash,\nHe laughed at Tommy with a thundering dash.\n\nBut Tommy just nodded, slow and polite,\n“I’ll get there too, just not with your might.”\nThrough woods and meadows, over a hill,\nHe kept moving forward, focused and still.\n\nThe rabbit got bored and took a quick nap,\nSnoring beneath a shady tree’s lap.\nWhile Tommy kept going with all of his heart,\nBelieving in patience and doing his part.\n\nStep after step, with time ticking on,\nThe sun in the sky and the dew nearly gone.\nTommy saw the finish, shining so bright,\nHe crossed it alone, to everyone's delight!\n\nThe forest all cheered, they clapped and they sang,\nWith bells and chimes that merrily rang.\nTommy just smiled, his head held up high,\nProof that the slow can reach the sky.",
  "moral": "Slow and steady wins the race."
},
{
  "title": "Sally and the Moon 🌙",
  "content": "Each night Sally climbed to her rooftop high,\nTo talk to the stars and the moon in the sky.\nShe whispered her wishes, her hopes and her fears,\nAnd trusted the moon with all of her tears.\n\n“I want to sing songs, loud, proud, and true,\nI want to do things that I dream I can do.\nBut fear holds me back like a heavy old chain,\nWill I ever be free, will I ever feel sane?”\n\nThe moon just glowed with a soft silver light,\nNodding gently through the hush of the night.\nThe stars blinked in rhythm, the wind sang along,\nAs if saying, “One day, you’ll be brave and strong.”\n\nSo Sally kept trying, day after day,\nPracticing notes in her own quiet way.\nShe sang to the trees, the birds, and the breeze,\nShe sang until her voice flowed with ease.\n\nThe big day arrived, the stage lights shone bright,\nSally stood ready, her heart full of fright.\nBut then she remembered the stars and the moon,\nAnd she sang her first note like a sweet monsoon.\n\nThe audience hushed, then rose to their feet,\nClapping and cheering her voice so sweet.\nSally bowed deeply, her eyes full of tears,\nHer dreams had come true beyond all her fears.\n\nThat night she whispered a thank-you above,\nTo the moon who had listened with patience and love.\nAnd the stars twinkled back in a shimmering row,\nSally the dreamer had stolen the show.",
  "moral": "Believe in your dreams—they can come true with time."
}

]

selected_story = random.choice(stories)
st.markdown(f"### *{selected_story['title']}*")
st.write(selected_story['content'])
st.markdown(f"💡 *Moral:* {selected_story['moral']}")

# --- 🎤 Voice Modulation ---
def generate_audio(text, filename="story.mp3"):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    return filename

if st.button("🎧 Listen to the Story"):
    full_text = f"{selected_story['title']}. {selected_story['content']}. Moral of the story: {selected_story['moral']}"
    audio_file = generate_audio(full_text)
    st.audio(audio_file, format="audio/mp3")

# Reload new story
if st.button("🔄 Load a New Story"):
    st.rerun()

# --- 🧠 Brain Game Section ---
st.markdown("---")
st.markdown("## 🧠 *Quick Brain Challenge!*")

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0, step=1)

if st.button("✅ Check Answer"):
    if user_answer == num1 + num2:
        st.success("🎉 Correct!")
    else:
        st.error("❌ Try again!")

# --- 👥 Social Skills Challenge ---
st.markdown("---")
st.markdown("## 👥 *Friendship & Social Skills!*")

qs, options = random.choice([
    ("Your friend seems sad. What do you do?",
     ["Ignore them", "Ask if they want to talk", "Make fun of them", "Tell them a joke"]),
    ("New student is alone. What should you do?",
     ["Walk away", "Introduce yourself", "Laugh at them", "Report them"]),
    ("Friend spilled your water. How do you react?",
     ["Yell", "Help clean", "Complain", "Stay quiet forever"])
])
user_choice = st.radio(qs, options)

if st.button("Submit Response"):
    good_choices = ["Ask if they want to talk", "Introduce yourself", "Help clean", "Tell them a joke"]
    if user_choice in good_choices:
        st.success("✅ Great choice! You’re a good friend.")
    else:
        st.error("❌ Hmm... maybe try a kinder response!")

# --- 🌱 Closing ---
st.markdown("---")
st.markdown("### 🚀 Keep Learning, Keep Growing! 🌱")
