# the \<wit\> project gateway project: "twitterish"


### 🖥 Install this project locally
1. Clone this repo: `git clone <this repo's remote url>`
2. Change directories: `cd gateway_project`
3. Create a virtual environment for this project and activate it:
```
mkdir env
python3 -m venv env
source env/bin/activate
```
4. Install the requirements: `pip install -r requirements.txt`
5. If you haven't done so already, create a database named `twitterish`
6. Run `python app/db.py` as needed to create and seed your database tables
7. Run the application as needed: `python app/app.py`
<br>

### 🖥 Set up your own personal branch
1. Create and checkout a personal branch: `git checkout -b gateway_project-<your name>`
2. Push up your personal branch: `git push origin gateway_project-<your name>`
3. Get the link for your personal branch on GitHub and paste it into the callout in the "Instructions" card on your kanban board

[Click here for a screenrecording of step 3.](https://drive.google.com/file/d/1yMrxBHp12mcMSF7nT-cZvJWXOc8lj7fs/view?usp=sharing)


### 🖥 Follow this workflow
1. Move any cards ready to be work on to the "Not started" column on your kanban board (you can probably do this by date)
2. Pick a card to work on from this column and move it to the "In progress" column on your kanban board
3. Create and checkout a feature branch for this card: `git checkout -b <your name>-<feature name>`
4. Make any changes and push it up to **this feature branch**:
```
git add -A
git commit -m "<commit message>"
git push origin <your name>-<feature name>
```
6. Open a pull request **against your personal branch** with a meaningful description, optionally get a review from your co-fellows, and merge!
7. Move your card to the "Completed" column. You did it!

[Click here for a screenrecording of step 6.](https://drive.google.com/file/d/1tMPOMCbHeRkY5togXQtwuD-FoWqImBBQ/view?usp=sharing).
