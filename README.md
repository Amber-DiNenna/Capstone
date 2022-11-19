# CAPSTONE 

# Kitchen Management Project Overview

This is a project that would make it easier for restaurant kitchen employees to communicate and know what to expect when heading into their shifts. It can also help kitchen managers clearly outline what is expected of employees during their shifts. 

Another main goal of this project is to be able to create a searchable database that allows the ability to connect/cross-reference ingredients/recipes/prep lists/inventory.

## GitHub Project Board Link

https://github.com/users/Amber-DiNenna/projects/1/views/1

## Technologies 

##### Django
##### Python
##### JavaScript
##### HTML
##### CSS

## Application Functionality

### Admin

Management can edit checklists, assign roles/access to users, add/edit recipes, edit inventory/prep lists.

### Users

User app would allow management to edit employee access to other applications, based on position or responsibilities. This would also support communication, transparency, and accountability by adding a timestamp and user name signature to whiteboard, notes, checklists, and prep list.

users
   - name
   - position
   - access to? 

### Home

Will render links for any apps the employee is allowed to see. 

### Whiteboard

A kind of kanban board with two main columns: 'TO DO' and 'NEEDS'. When each item is either added or checked off, a timestamp and user name will be attached. Should also have ability to 'undo' action. When checked off, item will be faded and moved to the bottom of the list, to ultimately be "erased" by a manager. 

whiteboard {
   to do: {
   item: (from prep list or manually added)
   date added: (timestamp)
   added by: (user name)
   completed: bool
   date completed: (timestamp)
   completed by: (user name)
      }
   
   needs: {
      item: (from inventory or manually added)
      date added: (timestamp)
      added by: (user name)
      completed: bool
    }
   }

### UPDATES: 86'd / Welcomings / Changes List

Blog format that provides communication between management/BOH/FOH about changes, attaching user name and timestamps to posts. Can color code to denote type of change. Include ability to attach photos. Chronological order allows employees coming in from their weekend/vacation to see all changes that happened during their absence.

posts
   - user name
   - type (86'd, new, change)
   - image tag
   - timestamp

### Checklists

Static opening and closing checklists with the ability for employees to "cross off" items with username and time stamp at the bottom. Incoming shift employees can "erase" to refresh list.

opening 
__ item
__ item 
__ item

completed by: _________________
timestamp: ________________

X CLEAR

### Inventory

A master stock list of ingredients organized by type of item/storage location (ie refrigerated, dry storage, low boy, prepped, etc.) Will have a fixed column for 'par' and column field for 'on hand'/'date by', as well as the ability to highlight items (with colors that denote 'low', 'out', '86d', 'dating soon'). Similar functionality as checklists, except items can be copied and added to whiteboard 'NEEDS' section.  

refrigerated
   - milk         par: 4 gal on hand: ___   X add to NEEDS   - highlight
   - cheese       par: 2 qts on hand: ___   X add to NEEDS   - highlight
   - sour cream   par: 1 qt  on hand: ___   X add to NEEDS   - highlight

dry storage
   - salt         par: 1 box on hand: ___   X add to NEEDS   - highlight
   - pepper       par: 1 box on hand: ___   X add to NEEDS   - highlight
   - fryer oil    par: 4 box on hand: ___   X add to NEEDS   - highlight

other
   - baguettes    par: 4 loaves on hand: ___   X add to NEEDS   - highlight
   - buns         par: 4 bags   on hand: ___   X add to NEEDS   - highlight

prepped (line)
   - sliced pork        par: 1 1/6 pan on hand: ___   X add to TO DO   - highlight
   - ranch              par: 1 bottle  on hand: ___   X add to TO DO   - highlight
   - beet vinaigrette   par: 1 bottle  on hand: ___   X add to TO DO   - highlight

prepped (walk-in)
   - pickled beets      par: 4 gal on hand: ___   X add to TO DO   - highlight
   - ranch              par: 2 qts on hand: ___   X add to TO DO   - highlight
   - beet vinaigrette   par: 1 qt  on hand: ___   X add to TO DO   - highlight

completed by: _________________
timestamp: ________________
   
X CLEAR

### Prep List

A master prep list with components organized by menu items/headers. Menu item links to image and details. Components link to recipe 'card'. Same functionality as INVENTORY list, except items can be copied and added to whiteboard 'TO DO' list.

appetizers
   - ploughmans plate 
      -- pickle beets    X add to TO DO
      -- slice cheese    X add to TO DO
      -- slice meat      X add to TO DO
      -- slice bread     X add to TO DO
      -- pickle olives   X add to TO DO
      -- pickle cabbage  X add to TO DO
   
   - rarebit
      -- cheese sauce   X add to TO DO
      -- cut chives     X add to TO DO
      -- slice bread    X add to TO DO
      
entrees
   - grain bowl
      -- mix grains     X add to TO DO
      -- cook brains    X add to TO DO
      -- make beet vin  X add to TO DO
      -- roast veg      X add to TO DO
      
   - fish & chips
      -- thaw fish      X add to TO DO
      -- make batter    X add to TO DO
      
      
   
      

### Recipes

Searchable database that links to recipe 'cards'. Links can be added to prep list items. Maybe ability to hide amounts based on clearance?

recipes {
   item: 'pickled beets'
   component of: [ploughmans plate, salad, grain bowl]
   ingredients: [{ingredient: amount}, ]
   directions: ''
   prep time: ''
   cooking time: ''
   batch size: ''
   in use: true/false
   image link: 
}

#### BONUS: Order Sheets

Would like the ability to integrate CSV files from purveyors to create easy ordering guides.

#### BONUS: Notes

Allows general notes to be viewable to staff or personalized notes to be sent between individual employees.

#### BONUS: Scheduling Calendar

Utilize a calendar API to provide a schedule that is viewable to employees.

#### BONUS: Employee Contact List

List employee names, positions, phone numbers, emails, avalability, and willingness to pick up shifts.

#### BONUS: Purveyor Contact List
