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
  { name: "Priya S.", background: "backgrounds/06-lilac-blush.png" },
```

If you make a mistake — more guests than images, a duplicate name, the same
image given to two people — **the page tells you at the top in an orange box**
when you open it. Nobody else will see it once it's fixed.

---

## 3. Use your own images

The 12 images in `backgrounds/` are placeholders so the page works right away.
To use real ones:

- Drop your images into the `backgrounds/` folder (on GitHub: **Add file** &rarr;
  **Upload files**).
- List each filename in the `BACKGROUNDS` array in `guests.js`.
- Make sure there are **at least as many images as guests**.

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
