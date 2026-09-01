# Baby Shower Zoom Backgrounds

A tiny public web page where each coworker taps their name and gets their **own**
Zoom background — no two people get the same one.

No server, no signups, no cost. It's a plain page hosted free by GitHub Pages.

---

## 1. Turn the page on (one time, ~30 seconds)

1. Go to your repo on GitHub &rarr; **Settings** &rarr; **Pages** (left sidebar).
2. Under **Build and deployment** &rarr; **Source**, choose **Deploy from a branch**.
3. Pick the branch from the dropdown, set the folder to `/ (root)`, and click **Save**.
4. Wait a minute, then refresh. GitHub shows you the live link, which will be:

   `https://jenimattson.github.io/BabyShowerBackground/`

> **Which branch?** The repo started out empty, so the first branch pushed to it
> became the default: `claude/github-zoom-background-picker-5kxx6j`. That works
> fine, but if you'd rather it be called `main` (tidier, and it's what most
> GitHub instructions assume), rename it first: **Settings** &rarr; **General**
> &rarr; **Branches** &rarr; the pencil icon next to the branch name. Then pick
> `main` in the Pages dropdown.

Share that link and you're done. Anyone can open it — no GitHub account needed.

> The repo has to be **public** for free GitHub Pages. That means anyone with the
> link can see the guest list, so the sample uses first name + last initial.
> Keep it that way if you'd rather not publish full names.

---

## 2. Add your coworkers

Edit **`guests.js`** — it's the only file you ever need to touch. You can do it
right in the browser: click the file on GitHub, click the pencil icon, type,
then **Commit changes**. The page updates itself about a minute later.

```js
const GUESTS = [
  "Alex R.",
  "Sam T.",
  "Jordan K.",
];
```

One line per person. **That's the whole job.** Everyone automatically gets their
own image from the pool, in order, and nobody shares. Add a name, and they get
the next unused one.

Want to hand-pick someone's image instead? Write their line like this:

```js
  { name: "Priya S.", background: "backgrounds/pirate.jpg" },
```

**Jess is already pinned** to her skiing illustration, so she always gets that
one and it never goes to anybody else:

```js
  { name: "Jess", background: "backgrounds/jess-skiing.png" },
```

If you make a mistake — more guests than images, a duplicate name, the same
image given to two people, or **a filename that isn't actually in the folder** —
the page tells you at the top in an orange box when you open it, naming the
exact file. Nobody else sees it once it's fixed.

---

## 3. Use your own images

1. On GitHub, **click into the `backgrounds/` folder first**, then **Add file**
   &rarr; **Upload files**. If you upload from the repo's front page instead, the
   files land loose in the root and the page won't find them.
2. Drag your images in and **Commit changes**.
3. List each filename in the `BACKGROUNDS` array in `guests.js`.
4. Make sure there are **at least as many images as guests**.

### If the upload fails or stalls

That's a size problem, and it's fixable. GitHub's web uploader caps a single
file at 25 MB and gets unreliable well before that across a whole batch.
Illustrations straight out of an AI generator are commonly 2-6 MB each as PNG,
so a dozen of them is 30-70 MB and the upload gives up.

Two ways through it:

- **Upload a few at a time.** Five or so per commit goes through fine.
- **Shrink them first**, which is worth doing anyway:

  ```bash
  pip install pillow
  python3 tools/optimize_backgrounds.py
  ```

  It rescales anything larger than 1920&times;1080, re-saves as JPEG, updates the
  matching filenames in `guests.js`, and writes small thumbnails into
  `backgrounds/thumbs/` for the name list. On this repo's images it took
  2.2&nbsp;MB files down to about 230&nbsp;KB with no visible difference —
  50&nbsp;MB of art became 8&nbsp;MB.

Size matters after the upload too: everyone opening the page loads a thumbnail
for each guest, and most of them will be on a phone. Thumbnails keep that down
to a few kilobytes each instead of a few megabytes.

**What makes a good Zoom background:** 16:9, JPG, ideally under 500&nbsp;KB.
Keep the middle fairly plain &mdash; that's where the person's face goes.

To delete an image, click it on GitHub and use the **&hellip;** menu &rarr; **Delete file**.
Remember to remove its filename from `BACKGROUNDS` too.

## Letting people pick their own (optional)

Out of the box everyone gets a unique image that's already assigned to them.
If you'd rather guests **choose** — and have an image lock the moment someone
takes it, so nobody can end up with the same one — that needs one free service,
because a GitHub Pages site can hand files out but can't take anything back.
Every visitor's browser gets its own copy of the page, so "Kelly took the
pirate" has to be written down somewhere all the browsers can see.

Roughly five minutes, once:

1. Go to **console.firebase.google.com** and sign in with a Google account.
2. **Create a project**. Any name. Turn off Google Analytics when it offers —
   you don't need it.
3. In the left sidebar: **Build** &rarr; **Realtime Database** &rarr;
   **Create Database**. Pick the region closest to you and choose
   **Start in locked mode**.
4. Open the **Rules** tab, replace what's there with this, and click **Publish**:

   ```json
   {
     "rules": {
       "claims": {
         ".read": true,
         "$image": {
           ".write": "!data.exists()",
           ".validate": "newData.hasChildren(['guestId', 'guestName'])"
         }
       }
     }
   }
   ```

   This is the bit that matters: `"!data.exists()"` means an image can be
   claimed **only if nobody has claimed it yet**. The refusal happens on
   Google's servers, so if two people tap the same picture in the same second,
   one of them genuinely loses — the page tells them who beat them to it and
   sends them back to choose again.

5. Back on the **Data** tab, copy the URL at the top. It looks like
   `https://your-project-default-rtdb.firebaseio.com`.
6. Paste it into `guests.js`:

   ```js
   const FIREBASE = {
     databaseURL: "https://your-project-default-rtdb.firebaseio.com",
   };
   ```

That's it. The page switches to picking on its own.

**What guests see:** they tap their name, then a board of every background.
Taken ones are greyed out and labelled with who has them. Tapping a free one
claims it on the spot and shows them their image with the download button.
The board refreshes every few seconds, so people watch it fill up.

Jess is skipped past all of this — she goes straight to her skiing background,
and it never appears on anyone else's board.

**To undo a pick** (someone changed their mind, or claimed the wrong one), open
the Firebase **Data** tab, find the entry under `claims`, and delete it. It
frees up again immediately.

**Worth knowing:** anyone with your page's link can claim an image — there's no
sign-in. That's the right trade for a baby shower, and the rule above means the
worst anyone can do is take an image, never overwrite someone else's. If you
want the picking to stop (say, everyone has chosen), empty the `databaseURL`
line and the page reverts to showing each person their claim.

## Nice things it already does

- **Personal links.** Every guest has their own URL, e.g.
  `…/BabyShowerBackground/?guest=alex-r` — it opens straight to their background.
  Text people their own link instead of making them hunt for their name. The
  **Copy my link** button on the page gets it for them.
- **Works on phones**, which is where most people will open it.
- **Built-in Zoom instructions** for desktop and mobile, right under the image.

---

## Wording

The title and subtitle come from the top of `guests.js`:

```js
const EVENT = {
  title: "Baby Shower",
  subtitle: "Pick your name to get your very own Zoom background",
  hostNote: "See you on the call! 🍼",
};
```

---

## One thing to know

This is a static page, so it hands out images from a list you set in advance —
it can't do first-come-first-served claiming, because there's no server keeping
track of who has clicked. Pre-assigning is actually the safer way round: nobody
can take someone else's, and nobody gets locked out.
