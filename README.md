# SIGN-LANGUAGE

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![HTML](https://img.shields.io/badge/Frontend-HTML%20%26%20CSS-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)

**Translate text into animated ASL, JSL, and ISL sign sequences.**

SIGN-LANGUAGE is an interactive Flask demonstration that converts typed phrases into region-specific, kinetic sign timelines. It includes an animated browser player, quick conversation templates, sign-language dictionary data, and a standalone text-to-animation helper.

> This project is a visual sign-sequence prototype. It does not provide certified sign-language interpretation or replace communication with a qualified interpreter.

## Why We Built It

Communication can become difficult in hospitals, schools, workplaces, public services, travel spaces, and everyday conversations. Spoken or written language is not equally accessible to everyone, and a shared method of communication is not always available at the moment it is needed.

Learning sign language can also be complex and demanding. Sign languages are complete natural languages with their own vocabulary, grammar, regional variations, facial expressions, body movement, and cultural context. Finding consistent learning resources and practicing accurate movements can take significant time and effort.

SIGN-LANGUAGE was built to make the learning and exploration process more approachable. It turns common typed phrases into visual sign sequences, allowing users to compare ASL, JSL, and ISL representations and understand the basic idea of regional sign communication. It aims to encourage awareness and practice while recognizing that real sign-language fluency requires direct, culturally informed human learning.

## Highlights

- Converts text into a word-by-word sign timeline
- Demonstrates American, Japanese, and Indian sign-language modules
- Uses region-specific labels and handshape representations
- Applies CSS animation patterns to kinetic hand icons
- Moves `where` to the end for the project's example question grammar
- Includes quick phrases for common conversations
- Provides an API endpoint for frontend and external integration
- Includes WLASL metadata and a small local animation dictionary

## How It Works

```text
Typed phrase
    |
    v
Flask API: POST /api/translate
    |
    v
Text cleanup and word matching
    |
    v
Regional dictionary lookup (ASL / JSL / ISL)
    |
    v
Ordered timeline of labels, hand icons, and motion styles
    |
    v
Browser kinetic player displays each sign in sequence
```

The Flask backend keeps regional mappings in `app.py`. `translator.py` provides a separate dictionary-based text-to-animation sequence generator using `dictionary.json`.

## Supported Demonstration Languages

| Module | Vocabulary coverage | Example output |
| --- | --- | --- |
| ASL | Hello, bathroom, where | Regional text labels and kinetic hand icons |
| JSL | Hello, bathroom, where | Japanese labels with region-specific motion |
| ISL | Hello, bathroom, where | Namaste-style and regional movement representations |

Unknown words are shown with a general fallback hand icon and an idle-breath animation.

## Quick Start

### Prerequisites

- Python 3.9 or newer
- pip

### 1. Clone the repository

```bash
git clone https://github.com/chauhanlegentyr-droid/SIGN-LANGUAGE.git
cd SIGN-LANGUAGE
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Flask

```bash
python -m pip install flask
```

### 4. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Try the Translator

1. Select ASL, JSL, or ISL.
2. Enter a phrase such as `hello bathroom where`.
3. Select **Animate Vector Signs**.
4. Watch the timeline play each matched sign for approximately 1.8 seconds.

Use the quick-conversation cards to load common examples.

## API

### Translate Text

```http
POST /api/translate
Content-Type: application/json
```

Example request:

```json
{
  "text": "hello bathroom where",
  "language": "ASL"
}
```

Example response:

```json
{
  "status": "success",
  "language": "ASL",
  "timeline": [
    {
      "label": "HELLO",
      "hand": "👋",
      "animation": "wave-motion"
    },
    {
      "label": "BATHROOM",
      "hand": "✊",
      "animation": "shake-motion"
    },
    {
      "label": "WHERE",
      "hand": "🤷",
      "animation": "shrug-motion"
    }
  ]
}
```

Try the endpoint:

```bash
curl -X POST http://127.0.0.1:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{"text":"where is the bathroom","language":"ASL"}'
```

## Standalone Sequence Helper

`translator.py` reads `dictionary.json` and converts text into matched words and animation filenames:

```bash
python translator.py
```

Example output:

```text
Typed Message: 'Where is the bathroom?'
Sign Language Word Order: ['bathroom', 'where']
Animation Queue to Play: ['bathroom_animation.json', 'where_animation.json']
```

## Project Structure

```text
SIGN-LANGUAGE/
├── app.py                 # Flask server, regional mappings, API, and UI
├── index.html             # Standalone frontend prototype
├── translator.py          # Dictionary-based text sequence helper
├── dictionary.json        # Word-to-animation filename mapping
├── WLASL_v0.3.json        # WLASL dataset metadata
└── animations/            # Reserved animation assets directory
```

## Included Data

- `dictionary.json` contains demonstration concepts for hello, where, bathroom, and thanks.
- `WLASL_v0.3.json` contains WLASL dataset information.
- `animations/` is reserved for future animation assets.
- The current interface uses emoji hand representations and CSS motion, rather than full 3D sign models.

## Limitations

- Sign languages are distinct natural languages with grammar rules that vary by region and community.
- The ASL, JSL, and ISL mappings provide a limited demonstration vocabulary.
- Emoji and CSS animations are visual approximations, not accurate anatomical sign representations.
- Unknown words do not receive validated signs and are shown with fallback animations.
- The prototype does not perform machine vision, gesture recognition, or real-time sign capture.
- The repository includes WLASL metadata but does not currently provide a complete trained WLASL recognition pipeline.

## Roadmap

- Replace emoji representations with 3D avatars or validated sign assets
- Expand vocabulary and regional grammar models
- Add accurate common-phrase and sentence-level sequences
- Integrate real avatar animation files
- Add real-time camera-based sign recognition
- Include cultural and accessibility guidance for each supported sign language
- Include unit tests for translation and grammar rules
- Add deployment configuration and pinned dependencies

## Developer

**Nirbhaysingh A. Chauhan**  
GitHub: [@chauhanlegentyr-droid](https://github.com/chauhanlegentyr-droid)

## Contributing

1. Fork the repository.
2. Create a focused feature branch.
3. Add validated vocabulary or animation assets.
4. Test API requests and browser playback.
5. Document regional and cultural context carefully.
6. Open a pull request with testing steps and screenshots.

## License

No license has been specified in this repository. Obtain permission from the owner before reuse or redistribution.
