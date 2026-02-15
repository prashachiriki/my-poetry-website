import streamlit as st

st.set_page_config(page_title="My Poetry Collection 🌸", layout="centered")

st.markdown("<h1>🌸 My Poetry Collection</h1>", unsafe_allow_html=True)
st.write("Browse my poems by mood/emotion 🌿")

poems = {

    "🌙 Soft / Peaceful / Hopeful": [

        """Spark vs Stability
we all go around the spark—
the spark—
which sets our body on fire.
it feels like the orange of the sunrise.
orange makes us feel the start of a new beginning,
which feels fresh,
turning minutes into seconds,
the world revolving around us.
as the sun begins to set down,
the dawn arrives—
the orange changes into blue.
the blue denotes the calm over chaos,
which pushes us back into reality.
the timing ticking a little longer,
the freshness fades away.
as the darkness arrives in black,
but—
we hold onto them in blue and black
to see the orange again.""",

        """Moon vs Sun
She finally found her answer — her type.
Someone who is more of a moon,
someone who lets her breathe.
Because she’s tired of the sun.
It felt too much,
yet she still left a piece of herself —
a piece that was consumed by the intensity.
And now, at last,
she wants someone who loves her in all her pieces,
like an unsolved puzzle,
and still makes her feel alive
without burning her out.""",

        """Moon Phases
Some days I’m a full moon — bright and warm.
I light up the whole sky.
People look at me and reminisce about their loved ones.
Some days, darkness comes along —
yet I still try to shine halfway,
I shine along with the stars.
Some days, darkness eats me up,
I darken the whole sky and scare people away.
But all along, I am still myself.
I always find my way back to the light —
but is it really my shine…
or just the sun’s?""",

        """Dear 2025
Dear 2025,
I stepped in with a ray of hope —
The beginning held a spark.
A spark that slowly turned into fire.
It ignited everything —
The comfort, peace, and love I found in a few people.
It left me burned,
Burns that still haven’t faded away.
But the good part is —
Those burns revealed the truth.
A truth that held my real self.
At dawn,
I stand here, all burned.
Yet one good thing remains —
The bad parts of me burned too.
Now I step toward 2026,
Holding onto my open wounds,
Hoping time will finally teach them how to heal."""
    ],

    "💔 Sad / Grief / Emotional Pain": [

        """Father’s Void
Life seems so normal.
But when I look back,
I still feel the void —
a father’s place.
I’ve never seen him,
yet I’ve heard of him.
Heard about the evil version of him,
the one that hurt others
and abandoned me.
He hurt my close people.
I should probably hate him, right?
Maybe I do.
But the little child in me still thinks —
maybe he wasn’t in the right state of mind.
At last, the little girl’s mind fills
with what-ifs.
Has he ever thought of us?
Did he feel regret?
All her what-ifs
lead to a dead end.""",

        """Falling
I felt lost.
I had no hand left to hold.
The touch I trusted
pushed me from the height.
Midair, I reached back —
still hoping, still believing —
trying to grasp that same hand.
But it did not hesitate to let me fall.
So I kept falling,
wondering why the hands
that once held me
chose to release me.
My heart filled with regret,
with questions that had no answers.
At the very end,
I saw the regret in their eyes —
and I left,
with peace in my last beat.""",

        """Too Broken
We neither have a future nor a past.
All we have is an illusion —
an illusion that feels so beautiful,
yet too surreal.
Because we’re both too broken,
still holding on to the past
while the present slips away."""
    ],

    "🌑 Dark / Lonely / Unseen": [

        """The Rat Race
The rat race—
I’m destined to something else, right?
Something dreamy, like fairytales.
Something that feels alive—
Something I don’t need escapism from.
But all the doors somehow lead to a dead end.
All I can find is a way to a rat hole.
Here, I feel drained, suffocated—
Yet it’s my only way to survive.
I struggle to compete,
But in the end, it doesn’t give me happiness.
Let’s still have hope together.
Maybe one day, we’ll become fireflies—
Flying into those dreamy feels,
Wild and free.""",

        """Love in Darkness
And then I realised,
My love only shines in darkness.
It stays silent in the light.
Too quiet for people to notice.
So I just linger away in the dark
Without leaving a trace.""",

        """The Art of Being Stuck
Being stuck on someone —
drained enough to know it’s all in vain.
Yet, the ocean in you still aches to give.
The sunshine in you still tries to fill their void.
At last, we are left with emptiness,
which is filled by their name.
In the end, you’re left as the version they loved —
not your true version."""
    ],

    "🌫 Nostalgic / Bittersweet / Longing": [

        """Déjà Vu
Some moments feel like déjà vu. They pull us back into a time we once lived —
a moment that held someone whose eyes carried stars,
someone who ran to me like a child,
held me close to their heart,
and even listened to my little yap,
as if every sound from me mattered.
Someone who was angry to let me go,
yet in the end, released me with eyes full of hope —
eyes that whispered, “When will we meet again?”
And that moment… it slowly turned into a memory.
A memory that can be replayed in the mind,
but never lived again in reality."""
    ]
}

for mood, poem_list in poems.items():
    st.markdown(f"### 🌿 {mood}")
    for idx, poem in enumerate(poem_list, start=1):
        st.markdown(f"*{idx}.* {poem}")
        st.markdown("---")

# Chat Section
st.markdown("<h2>🌸 Chat with me</h2>", unsafe_allow_html=True)
st.write("Share your mood or feelings and I’ll reply personally 🌿")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Enter your mood or feeling 🌿")

if st.button("Send Message"):
    if user_input:
        st.session_state.chat.append(f"💬 User: {user_input}")
        st.session_state.chat.append(
            "🌸 PoetryBot: I don’t have a poem for this yet. Please share more about your feelings so I can write you a personalized poem 🌿"
        )

for message in st.session_state.chat:
    st.write(message)
