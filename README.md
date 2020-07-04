# Wiki

Wiki is a Web Application built using Django for creating an online encyclopedia that consists of pages on various topics. A user can visit a URL for example `/wiki/TITLE` to see the content of that entry. The user also has the ability to create their own entries/pages by using **Create New Page** link. Finally, if a user clicks on **Random Page** they will be taken to a random page in the encyclopedia.

#### Entry Page

When a user visits `/wiki/TITLE`, where `TITLE` is the title of the encyclopedia entry, they will be taken to that entry's page. But if an entry is requested that does not exists, they will be displayed with an error message.

#### Index Page

When a user visits `/` route, they will be presented with a list of all the entries that exists in the encyclopedia. Clicking on any one of them will take them to the individual entry's content.

#### Search

The `/` route has a search bar that can used to find a particular entry. If the search string matches with the title of a particular entry, the user is redirected to that entry's page. Otherwise the application would display a list of potential matches by searching for partial matches.

#### New Page

When clicked on the **Create New Page** in the sidebar, the user is taken to the page where they can create a new encyclopedia entry. They can provide the title for that entry along with the `markdown` content in the textarea. If an entry with the same title already exists, the user would be displayed with an error message. Otherwise, a new entry will be saved to the disc.

#### Edit Page

The app provides the functionality to edit any entry by clicking on `edit this page` link on an individual entry's page. The user would be able to edit the markdown content of that page and submit it.

#### Random Page

Clicking on **Random Page** takes the user to a random entry within the encyclopedia.

#### Markdown to HTML Conversion

The application uses `markdown2` for converting the markdown content into HTML for each entry before it renders in the user's web browser. 
