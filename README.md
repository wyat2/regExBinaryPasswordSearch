# regExBinaryPasswordSearch
Password cracker.  Binary search efficient 

Author: Andrew Wyatt

My script designed to perform a blind NoSQL injection attack using a binary search technique to extract a password from a target web application.
It's a form of brute-force password guessing that is highly optimized.

Key Components and Functionality
1. main() Function
- Input: It requires a single command-line argument: the URL of the target site (e.g., localhost:8000).
- Target Construction: It takes the argument and constructs the full URL path, specifically targeting http://<wfp2_site>/mongodb/example2/, suggesting it's designed for a web application using a MongoDB database (as is common with NoSQL injection examples).
- Execution: It calls the search_url function to find the password and prints the final result.

2. search_url(url_name) Function
This is the core exploit logic:
- Character Set (test): It defines a range of characters to test: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@. The @ symbol is used as a terminating character to signal the end of the search.
- Binary Search Attack: Instead of checking one character at a time, it uses an efficient binary search (or more accurately, a modified binary check) to determine the next character.
- - In each loop, the current character set (found) is split in half (Half).
- - A HTTP GET request is sent to the target URL.
- - The request URL contains a specially crafted NoSQL injection payload in the search query parameter.

3. The Injection Payload (Crucial Part)
The code constructs a request URL with this pattern:

url_name + "?search=admin%27%20%26%26%20this.password.match(/^" + result + "[" + found[:Half] + "].*/)//+%00"

When URL-decoded, the core injection query is:

search=admin' && this.password.match(/^<result>[<first half of found>].*/)//

- admin': This is likely used to complete and close an existing query involving the username 'admin'.

- &&: This chains the original query with the attack's condition.

- this.password.match(/^<result>[...].*/): This is a MongoDB/JavaScript regular expression (RegEx) query that attempts to match the password field.

- - ^: Start of the string.

- - <result>: The part of the password already found in previous iterations.

- - [...]: A character class containing the first half of the test characters (found[:Half]).

- - .*: Matches any remaining characters.

//: This is a comment used to nullify the rest of the original query structure on the server side.

4. Brute-Force Logic
- Condition Check: The script checks the response body (j.text) for the substring "admin". In a blind attack, if the injection is successful and the condition is true (meaning the password matches the RegEx), the page is assumed to display content only accessible to the 'admin' user, confirming the character is in the first half.

- Narrowing the Range:

- - If "admin" is found ("Yes"), the search range (found) is narrowed to the first half.

- - If "admin" is not found ("No"), the search range is narrowed to the second half.

- Character Found: When the found string is narrowed down to a single character (len(found) == 1), that character is appended to the result string (the growing password), and the entire process repeats to find the next character.

In summary, it's a tool for penetration testing or security research that exploits a vulnerable NoSQL query to sequentially guess a password one character at a time with maximum efficiency.
