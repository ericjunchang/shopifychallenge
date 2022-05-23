# shopifychallenge including deletion, deletion comments and undeletion
Shopify Backend Developer Internship Challenge

Backend challenge from Shopify using Flask, Python, HTML/CSS and some JavaScript. Enjoy!

## How to run the app?
Locally
```bash
pip3 install -r requirements.txt
flask run -p 8080 --host=0.0.0.0
```
On repl.it
repl.it link: https://shopifychallenge-backendchallenge-ericjunchang.ericjunchang.repl.co

## How to use the app?
On the main landing page, you can first add an item into the inventory by adding in the name of the item, the item's reference number and the quantity of said item. If one or more pieces of information is missing, the item will not be added. Once the item is added, you can edit the item's name, reference number or quantity. It is also possible to archive (delete) the item with or without a comment. This will move the item from the inventory list to the archived inventory list which can be accessed by clicking on the Archived Inventory List button on the top right corner of the homepage. 

On the Archived Inventory List page, you have the possibility to unarchive (undelete) the item and move it back into the inventory list. It will prompt you for the quantity of said item prior to pushing it to the inventory list. Additionally, a button has been added on the rightmost column which allows you to permanently delete the item if it has been added in by mistake or for other reasons. Last, but not least, a button has been added on the topright corner to allow you to go back onto the mainpage. 
