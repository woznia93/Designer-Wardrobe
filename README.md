# Outfit Idea Generator

## Overview

The Outfit Idea Generator is a unique application that helps users create stylish and personalized outfit suggestions based on their existing wardrobe. By leveraging user preferences and OpenAI's DALL-E, the tool refines and generates outfit ideas tailored to the user's tastes.

## Features

- **Wardrobe Input**: Users can upload pictures of their clothes.
- **Outfit Suggestions**: The tool provides initial outfit ideas based on the uploaded wardrobe.
- **User Feedback Loop**: Users can approve or reject outfit suggestions:
  - Selecting "Yes" adds the outfit to a favorites list.
  - Selecting "No" discards the outfit.
- **AI Enhancement**: Using the favorites list, the tool inputs data into DALL-E from OpenAI to generate new, creative outfit ideas.
- **Continuous Improvement**: The cycle of generating and approving outfits continues until the user finds a satisfying DALL-E generated outfit.

## How It Works

1. **Upload Wardrobe**: Users upload pictures of their clothing items.
2. **Initial Suggestions**: The application generates initial outfit ideas from the uploaded wardrobe.
3. **User Feedback**: Users review and provide feedback on the suggested outfits:
    - **Yes**: The outfit is added to the favorites list.
    - **No**: The outfit is discarded.
4. **AI Generation**: The favorites list is sent to DALL-E, which generates new outfit ideas based on the user's preferences.
5. **Final Selection**: The process repeats until the user approves a DALL-E generated outfit.

## Getting Started

### Prerequisites

- Node.js
- Python
- OpenAI API key

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/outfit-idea-generator.git
    cd outfit-idea-generator
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the application**:
    ```bash
    npm start
    ```

### Usage

1. **Upload your wardrobe**: Navigate to the upload section and add pictures of your clothes.
2. **Review initial suggestions**: Approve or reject the initial outfit ideas.
3. **AI-generated outfits**: Review and approve or reject the outfits generated by DALL-E.
4. **Enjoy your personalized outfit**: Once satisfied with an outfit, save and enjoy your new look!

## Contributing

We welcome contributions to enhance the Outfit Idea Generator! To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Create a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for their incredible DALL-E API.
- [Node.js](https://nodejs.org/) and [Python](https://www.python.org/) for the development environment.
