import re
import json

MARKDOWN_CONTENT = """
# Bookmarklets

<br>
<details><summary>What is a Bookmarklet?</summary>
  <br>
A bookmarklet is a bookmark stored in a web browser that contains JavaScript commands that add new features to the browser. They are stored as the URL of a bookmark in a web browser or as a hyperlink on a web page. Bookmarklets are usually small snippets of JavaScript executed when user clicks on them - Wikipedia 
</details>

<details><summary>Procedure to Save a Bookmarklet</summary>
 <br>
1. Copy the code snippet and Goto the Bookmark section of your browser<br>
2. Create a bookmark with this code as the URL (you should have known how to do it :)<br>
3. Give whatever the name you want & Save it <br>
4. Booom Done, That's All folks 🦾<br>
5. Click and check the functionality of the code, It should work 100% <br>
</details>

<details><summary>Want to collaborate in this Repo?</summary>
 <br>
1. Fork and commit in your repo <br>
2. Changes will be reviewed and accepted based on the effectiveness of the content 
</details>
<details><summary>Geneate Bookmarklets here</summary>
<a href='https://caiorss.github.io/bookmarklet-maker/'>https://caiorss.github.io/bookmarklet-maker/</a> <br>
  </details>
<br>

## List of Bookmarklets 👇

### 1. EasyTimer⌚
This works with any browser with Javascript support, Like Chrome, Firefox, Edge, Brave etc...

#### Code Snippet :
```
javascript: const input = prompt("Enter minutes: ");url="https://www.google.com/search?q=set+timer+for+%22+%20input%20+%22+minutes%22;window.open(url,%20%27_blank%27).focus();
```
>Thank Google for Timer component & Thank me for making the process easier <br>

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 2. Turn Off Personalised Web Search results 
Sometimes these Personalisations goes out of hand and shows unwanted Highlights in the webpages,That might be annoying for some guys like me, This Feature turns off the PWS feature in a single click

#### Code Snippet :
```
javascript:(function(){window.location=document.URL+'?pws=0%27%20})()
```
[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 3. Colour Picker by Google 🌈
You know? Google has a colour picking tool which can be used to get colour codes in many formats by eyedropping, Access this feature in a single click

#### Code Snippet :
```
javascript:(function(){window.location='https://www.google.com/search?q=color+picker'})()
```

>Thank Google for Color Picking Feature & Thank me for making the process easier <br>

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 4. Calculator by Google ➗
This is a great feature made by Google, we can use scientific / general calculator on web without getting into any sites, Access this feature in a single click

#### Code Snippet :
```
javascript:(function(){window.location='https://www.google.com/search?q=calculator'})()
```

>Thank Google for Calculator Component & Thank me for making the process easier <br>

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 5. Unit Conventor by Google ※
This is also a great feature made by Google, we can convert Currencies, Weight, Length in other units on web without getting into any sites, Access this feature in a single click

#### Code Snippet :
```
javascript:(function(){window.location='https://www.google.com/search?q=Unit%20converter'})()
```

>Thank Google for Unit Convertor Component & Thank me for making the process easier <br>

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 6. Text Anchors ⚓ 
A hidden feature used by Search Engine to highlight & direct the users to a specific part of the Page which is related to their query, While using this feature, You should be at the webpage & the text to be anchored should be copied before clicking it <br>
This will be useful when you need to hyperlink an exact part of the website to your friend, After clicking the bookmarklet, you can copy & share the new link to friend, It will highlight the text in the page which was provided by you
#### Code Snippet :
```
javascript:const input = prompt("Enter the text to be anchored (maximum 10 words):  ");(function(){window.location=document.URL+'#:~:text='+input})()
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 7. Enable Right Click 😉
Some websites may block you from Right Click & using Context Menu aka Right click menu, But we can enable it again by using this simple Bookmarklet
#### Code Snippet :
```
javascript:(function(){var d=document;d.onmousedown=null;d.onmouseup=null;d.oncontextmenu=null})()
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 8. Birthday Moon Phase 🌒
If you are eager to see how the Moon looked when you were born, Check this out. You can use both of them, Second one has moon images of any date<br>
Credits: [Lunaf](https://lunaf.com/lunar-calendar/) & [MoonPhase](https://phasesmoon.com/)
#### Code Snippet :
```
javascript:const input = prompt("Enter date(YYYY/MM/DD only works):  ");(function(){window.location='https://lunaf.com/lunar-calendar/'+input})()
```
```
javascript:const input = prompt("Enter date(eg: 3March1978) without spaces:  ");(function(){window.location='https://phasesmoon.com/moonday'+input+'.html'})()
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 9. Google Search Handy Shortcuts⚡
Web Surfing can sometime be frustating if we want to click & navigate through many Tabs, Here are some handy shortcuts to directly get what we want
#### Code Snippet to Search Images:
```
javascript:const input = prompt("Enter the Query : ");window.location='https://www.google.com/search?q='+input+'&tbm=isch'
```
#### Code Snippet Search Images with Creative Commons Licence:
```
javascript:const input = prompt("Enter the Query : ");window.location='https://www.google.com/search?q='+input+'&tbm=isch&tbs=il:cl'
```
#### Code Snippet to Search Transparent Images:
```
javascript:const input = prompt("Enter the Query : ");window.location='https://www.google.com/search?q='+input+'tbm=isch&tbs=ic:trans'
```
#### Code Snippet for Direct Video Search:
```
javascript:const input = prompt("Enter the Query : ");window.location='https://www.google.com/search?q='+input+'tbm=vid'
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 10. Developers' Search (YouCode)⚡

#### Code Snippet for Direct Getting results tailored for a Dev, like Code snippets, Tutorials, Articles etc.. :
```
javascript: const input = prompt("Enter Query: ");url="https://you.com/search?q=%22+input;window.open(url,%20%27_blank%27).focus();
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 11. Tech Stack Lookup (builtwith) ⚡

#### Code Snippet for Looking up the tech Stack for any website :
```
javascript:url="https://builtwith.com/?%22+document.URL;window.open(url,%20%27_blank%27).focus();
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 12. HTML Preview by [Github](https://htmlpreview.github.io/)⚡
Note: You have to upload HTML files to github and currently at the page where HTML file is located.

#### Code Snippet for previewing HTML pages directly from Github :
```
javascript:url="https://htmlpreview.github.io/?%22+document.URL;window.open(url,%20%27_blank%27).focus();
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 13. Download all images from any site in a single click

#### Code Snippet:
```
javascript:;(function() {var images = [].slice.call(document.querySelectorAll('img'));try {images.forEach(function(img){downloadImage(img)})} catch (e) {alert('Download failed.');console.log('Download failed.', e)}function downloadImage(img) {var link = document.createElement('a');link.setAttribute('href', img.src);link.setAttribute('download', '');link.click()}}).call(window);
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>


### 14. Share current Tab's URL to Whatsapp⚡

#### Code Snippet :
```
javascript:url="https://wa.me/?text=%22+document.URL;window.open(url,%20%27_blank%27).focus();
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 15. Search for a specific filetype 🔎

#### Code Snippet :
```
javascript:const input = prompt("Enter Query : "); const type = prompt("Extension type"); window.location='https://www.google.com/search?q=%27+input+%27%20ext%3A%27+type
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>

### 16. Find a free vector icon superfast (using Iconfinder) ✨

#### Code Snippet :
```
javascript:const input = prompt("Search in IconFinder : ");(function(){window.location='https://www.iconfinder.com/search?q=%27+input+%27&price=free%27})()
```

[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈<br>
Still having doubts - [Contact Me](https://wa.me/919345160259/)

<hr style="border:2px solid gray"> </hr>
<br>
"""

def generate_id(title_str):
    title_no_emoji = title_str.encode('ascii', 'ignore').decode('ascii').strip()
    id_str = title_no_emoji.lower()
    id_str = id_str.replace("'", "")
    id_str = re.sub(r'&', 'and', id_str)
    id_str = re.sub(r'[^\w\s-]', '', id_str) 
    id_str = re.sub(r'\s+', '-', id_str) 
    id_str = re.sub(r'-+', '-', id_str)
    return id_str.strip('-')

def add_bookmarklet(bookmarklets, title, desc_lines, code_snippets_list):
    # Helper to finalize and add a bookmarklet to the list
    
    # Process description
    description = " ".join(desc_lines).strip()
    # Filter out common unwanted phrases from description that might have been caught
    unwanted_phrases = [
        ">Thank Google for Timer component & Thank me for making the process easier",
        ">Thank Google for Color Picking Feature & Thank me for making the process easier",
        ">Thank Google for Calculator Component & Thank me for making the process easier",
        ">Thank Google for Unit Convertor Component & Thank me for making the process easier",
        "[**Procedure**](https://github.com/hariprasd/cool-bookmarklets#bookmarklets) 👈",
        "Still having doubts - [Contact Me](https://wa.me/919345160259/)"
    ]
    for phrase in unwanted_phrases:
        description = description.replace(phrase, "").strip()
    description = re.sub(r'\s{2,}', ' ', description) # Replace multiple spaces with one


    # Process snippets
    final_snippets = []
    for snippet_text in code_snippets_list:
        clean_snippet = snippet_text.strip()
        if clean_snippet: # Ensure snippet is not empty
            if not clean_snippet.startswith("javascript:"):
                clean_snippet = "javascript:" + clean_snippet
            final_snippets.append(clean_snippet)
            
    if not title or not final_snippets: # Must have title and at least one valid snippet
        return

    bookmarklet_id = generate_id(title)
    if not bookmarklet_id: # Must have a valid ID
        return
        
    bookmarklets.append({
        "id": bookmarklet_id,
        "title": title.strip(),
        "description": description,
        "code_snippets": final_snippets
    })

def parse_markdown_to_json(markdown_text):
    bookmarklets = []
    lines = markdown_text.splitlines()

    current_title = None
    current_description_lines = []
    current_code_block_lines = []
    is_in_code_block = False
    is_google_search_shortcuts = False
    base_desc_for_google = [] # Store main description for Google Search Handy Shortcuts

    # Find the starting line
    start_line_idx = 0
    for idx, line in enumerate(lines):
        if line.strip() == "## List of Bookmarklets 👇":
            start_line_idx = idx + 1
            break
    
    for i in range(start_line_idx, len(lines)):
        line = lines[i] # Keep original spacing for code blocks, strip later for others
        stripped_line = line.strip()

        if stripped_line.startswith("### "):
            # Finalize previous bookmarklet before starting a new one
            if current_title and not is_google_search_shortcuts: # Google shortcuts are handled differently
                add_bookmarklet(bookmarklets, current_title, current_description_lines, ["\n".join(current_code_block_lines)] if current_code_block_lines else [])

            # Reset for new bookmarklet
            current_title = re.sub(r"### \d*\.?\s*", "", stripped_line).strip()
            current_description_lines = []
            current_code_block_lines = [] # Reset for general snippets
            is_in_code_block = False
            is_google_search_shortcuts = "google search handy shortcuts" in current_title.lower()
            if is_google_search_shortcuts:
                base_desc_for_google = [] # Reset/start collecting base description for this group
            continue

        if not current_title: # Skip lines until the first title is found
            continue

        # Handle Google Search Handy Shortcuts sub-items
        if is_google_search_shortcuts:
            if stripped_line.startswith("#### Code Snippet"):
                # This is a sub-item of Google Search Handy Shortcuts
                sub_title_match = re.match(r"####\s*Code Snippet(?:s\s*to|s\s*for|s\s*by|:)?\s*(.*?):", stripped_line, re.IGNORECASE)
                if sub_title_match:
                    sub_title_detail = sub_title_match.group(1).strip()
                    # The snippet for this sub-item is expected to be next
                    # Look ahead for its ```javascript block
                    temp_sub_code_lines = []
                    for j in range(i + 1, len(lines)):
                        sub_line_stripped = lines[j].strip()
                        if sub_line_stripped.startswith("```javascript"):
                            # Start of snippet for sub-item
                            for k in range(j + 1, len(lines)):
                                code_line = lines[k] # Preserve internal newlines
                                if code_line.strip() == "```":
                                    # End of snippet for sub-item
                                    full_sub_title = f"{current_title}: {sub_title_detail}" if sub_title_detail else current_title
                                    # Use the collected base_desc_for_google as description
                                    add_bookmarklet(bookmarklets, full_sub_title, base_desc_for_google, ["\n".join(temp_sub_code_lines)])
                                    i = k # Advance outer loop
                                    break # Exit k loop
                                temp_sub_code_lines.append(code_line)
                            break # Exit j loop
                        elif sub_line_stripped.startswith("####") or sub_line_stripped.startswith("###"):
                            break # Next sub-item or main item started before snippet found
                    continue # Continue outer loop from advanced i

            elif not stripped_line.startswith("```") and not stripped_line.startswith("<hr") and not stripped_line.startswith("[**Procedure**]") and not stripped_line.startswith("Still having doubts"):
                 # This is part of the main description for Google Search Handy Shortcuts
                base_desc_for_google.append(stripped_line)
            continue # End of Google Search specific handling for this line

        # General bookmarklet processing (non-Google Search Handy Shortcuts)
        if stripped_line.startswith("#### Code Snippet"):
            # This header indicates description part is over for the current item
            # Snippet content will be handled by ```javascript block
            current_code_block_lines = [] # Reset for a new snippet block potentially
            is_in_code_block = False
            continue

        if stripped_line.startswith("```javascript"):
            is_in_code_block = True
            current_code_block_lines = [] # Start collecting new snippet
            # Handle code on the same line as ```javascript
            code_on_same_line = stripped_line[len("```javascript"):].strip()
            if code_on_same_line: # If there's code after ```javascript on the same line
                if code_on_same_line.endswith("```"): # e.g. ```javascript ... ```
                    current_code_block_lines.append(code_on_same_line[:-3].strip()) # Add code, remove trailing ```
                    # This snippet is complete, add it to the list for the current bookmarklet
                    # This assumes one snippet per ``` block for general items
                    add_bookmarklet(bookmarklets, current_title, current_description_lines, ["\n".join(current_code_block_lines)])
                    current_code_block_lines = [] # Reset for next potential snippet
                    is_in_code_block = False 
                else: # e.g. ```javascript ...
                     current_code_block_lines.append(code_on_same_line)
            continue

        if stripped_line == "```" and is_in_code_block:
            is_in_code_block = False
            # For general items, a ``` might mean the end of all snippets for that item, or one of many.
            # The problem asks for a list of snippets. "Birthday Moon Phase" has two.
            # My current logic for general items might need adjustment if it assumes one snippet per item.
            # Let's try to collect all snippets for a general item until next ###.
            # The add_bookmarklet is called when new ### is hit.
            # So, current_code_block_lines should be added to a list of snippets for current_title
            # This part is tricky with the current structure.
            # Let's assume for now that if a code block ends, we store it and a new one might start.
            # The current structure is more geared to one main code block or Google's special case.

            # For "Birthday Moon Phase", it has two ``` blocks.
            # The current add_bookmarklet takes a list.
            # The problem is WHEN to call add_bookmarklet for multi-snippet general items.
            
            # Re-thinking: for general items, collect all snippets until next ###.
            # So, if code block ends, add its content to a temporary list for current_title.
            # This means current_code_block_lines should be a list_of_lists_of_lines or list_of_strings
            
            # Simpler: if code block ends, we treat its content as one snippet string.
            # The main loop's end condition (next ###) will call add_bookmarklet, which takes a list of strings.
            # So, we need a list to hold these snippet strings for the current_title.
            
            # Let's use a temporary list `temp_snippets_for_current_item`
            if 'temp_snippets_for_current_item' not in locals() or current_title != (locals().get('last_title_for_temp_snippets', '')):
                temp_snippets_for_current_item = []
                last_title_for_temp_snippets = current_title

            if current_code_block_lines:
                 temp_snippets_for_current_item.append("\n".join(current_code_block_lines))
            current_code_block_lines = [] # Reset for next potential snippet block
            continue


        if is_in_code_block:
            current_code_block_lines.append(line) # Add raw line to preserve formatting
            continue

        # If not in code block, and not a header, it's part of description (if current_title is active)
        if current_title and not is_google_search_shortcuts: # Description for general items
            if not stripped_line.startswith("<hr") and \
               not stripped_line.startswith((">Thank Google", "[**Procedure**]", "Credits:", "Still having doubts")):
                current_description_lines.append(stripped_line)

    # Add the very last bookmarklet after the loop finishes
    if current_title:
        if is_google_search_shortcuts:
            # Google shortcuts are added as they are found. Nothing to do here.
            pass
        else:
            # Need to use the temp_snippets_for_current_item collected
            snippets_to_add = []
            if 'temp_snippets_for_current_item' in locals() and last_title_for_temp_snippets == current_title:
                snippets_to_add.extend(temp_snippets_for_current_item)
            if current_code_block_lines: # any unfinished snippet
                snippets_to_add.append("\n".join(current_code_block_lines))
                
            add_bookmarklet(bookmarklets, current_title, current_description_lines, snippets_to_add)

    return bookmarklets

if __name__ == '__main__':
    # This is the only print statement that should be active.
    # It outputs the final JSON data to stdout.
    parsed_data = parse_markdown_to_json(MARKDOWN_CONTENT)
    print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
