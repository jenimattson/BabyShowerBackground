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
  { name: "Priya S.", background: "backgrounds/06-pine-mist.png" },
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

The 12 images in `backgrounds/` are placeholders so the page works right away.
They're tinted to match the illustrations — cream paper, alpine blues — but
they're meant to be replaced. To use your real ones:

1. On GitHub, open the `backgrounds/` folder &rarr; **Add file** &rarr; **Upload files**.
2. Drag in your images (you can drop the whole batch at once) and **Commit changes**.
3. In `guests.js`, list each filename in the `BACKGROUNDS` array.
4. Make sure there are **at least as many images as guests**.

Jess's file needs to be named exactly **`jess-skiing.png`** to match the line
that's already pinned to her — or change that line to whatever you name it.

Short filenames with no spaces work best: `jess-skiing.png`, not
`Baby Shower FINAL (2).png`. If a name doesn't match, the orange box on the page
will tell you which file it couldn't find.

**What makes a good Zoom background:** 1920&times;1080 pixels (16:9), JPG or PNG,
under about 2&nbsp;MB. Keep the middle fairly plain — that's where the person's
face goes — and put the decoration around the edges.

To delete a placeholder, click it on GitHub and use the **&hellip;** menu &rarr; **Delete file**.
Just remember to remove its filename from `BACKGROUNDS` too.

---

## Nice things it already does

- **Personal links.** Every guest has their own URL, e.g.
  `…/BabyShowerBackground/?guest=alex-r` — it opens straight to their background.
  Text people their own link instead of making them hunt for their name. The
  **Copy my link** button on the page gets it for them.
- **Search box**, for when the list gets long.
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

## Regenerating the placeholders

Only if you want more or different placeholder images:

```bash
pip install pillow
python3 tools/make_placeholder_backgrounds.py
```

Edit the `PALETTES` list in that script to change the colors or add more.

---

## One thing to know

This is a static page, so it hands out images from a list you set in advance —
it can't do first-come-first-served claiming, because there's no server keeping
track of who has clicked. Pre-assigning is actually the safer way round: nobody
can take someone else's, and nobody gets locked out.
