# Spotify.Playlist.Generator🎵

<p>Spotify Playlist Generator automatically create a Spotify playlist based on the Billboard Top 100 songs from a specific date chosen by the user.</p>

</p>Key Features:

  - User Input: Prompts the user to enter a date in the format YYYY-MM-DD.

  - Top 100 Retrieval: Uses the Top_100 class (from top_100.py) to get the Billboard Top 100 songs for the given date.

 - Spotify Integration: Authenticates with the user's Spotify account using OAuth and the Spotipy library.

  - Track Search: Searches Spotify for each Billboard song to find the correct tracks.

 - Playlist Creation: Creates a new private playlist in the user's Spotify account named after the selected date and adds all found tracks to it.


**Dependencies:**

  - spotipy for Spotify API interaction

  - dotenv for loading environment variables (Spotify credentials)

  - A custom Top_100 class to retrieve song lists</p>
