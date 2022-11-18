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

## Applications

### Users

User app would allow management to edit employee access to other applications, based on position or responsibilities. This would also support communication, transparency, and accountability by adding a timestamp and user name signature to whiteboard, notes, checklists, and prep list.

### Home

Will render links for any apps the employee is allowed to see. 

### Whiteboard

A kind of kanban board with two main columns: 'TO DO' and 'NEEDS'. When each item is either added or checked off, a timestamp and user name will be attached. Should also have ability to 'undo' action. When checked off, item will be faded and moved to the bottom of the list, to ultimately be "erased" by a manager. 

### 86'd / Welcomings / Changes List

Blog format that provides communication between management/BOH/FOH about changes, attaching user name and timestamps to posts. Can color code to denote type of change. Include ability to attach photos. Chronological order allows employees coming in from their weekend/vacation to see all changes that happened during their absence.

### Checklists

Static opening and closing checklists with the ability for employees to "cross off" items with username and time stamp at the bottom. Incoming shift employees can "erase" to refresh list.

### Inventory

A master stock list of ingredients organized by type of item/storage location (ie refrigerated, dry storage, low boy, prepped, etc.) Will have a fixed column for 'par' and column field for 'on hand'/'date by', as well as the ability to highlight items (with colors that denote 'low', 'out', '86d', 'dating soon'). Similar functionality as checklists, except items can be copied and added to whiteboard 'NEEDS' section.  

### Prep List

A master prep list with components organized by menu items/headers. Provide link to recipe 'card'. Same functionality as INVENTORY list, except items can be copied and added to whiteboard 'TO DO' list.

### Recipes

Searchable database that links to recipe 'cards'. Links can be added to prep list items. Maybe ability to hide amounts based on clearance?

recipes {
   item:
   component of: []
   ingredients: []
   directions:
   prep time:
   cooking time:
   batch size:
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
