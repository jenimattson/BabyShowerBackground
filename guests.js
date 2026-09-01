/* ============================================================
   THIS IS THE ONLY FILE YOU NEED TO EDIT.
   ============================================================

   1. EVENT  — the words on the page.
   2. BACKGROUNDS — the pool of images in the backgrounds/ folder.
   3. GUESTS — one line per person.

   Everyone on the GUESTS list automatically gets their own image
   from the pool, in order. Nobody shares. You just type names.
   ============================================================ */

const EVENT = {
  title: "Baby Shower",
  subtitle: "Pick your name to get your very own Zoom background",
  hostNote: "See you on the call! \u{1F37C}",
};

/* The image files, in the order they get handed out.
   Add more files to the backgrounds/ folder, then add the
   filename here so there are at least as many images as guests. */
const BACKGROUNDS = [
  "backgrounds/01-blush-clouds.png",
  "backgrounds/02-mint-dots.png",
  "backgrounds/03-sky-lavender.png",
  "backgrounds/04-butter-peach.png",
  "backgrounds/05-sage-oat.png",
  "backgrounds/06-lilac-blush.png",
  "backgrounds/07-seafoam-sky.png",
  "backgrounds/08-apricot-cream.png",
  "backgrounds/09-periwinkle-cloud.png",
  "backgrounds/10-rose-sand.png",
  "backgrounds/11-pistachio-butter.png",
  "backgrounds/12-dusty-blue-shell.png",
];

/* One line per person. Just the name is enough.
   Tip: first name + last initial keeps the page a bit more private,
   since anyone with the link can read it.

   Want to hand-pick someone's image instead of letting it
   auto-assign? Write that line like this:
     { name: "Priya S.", background: "backgrounds/06-lilac-blush.png" },
*/
const GUESTS = [
  "Alex R.",
  "Sam T.",
  "Jordan K.",
  "Priya S.",
  "Miguel A.",
  "Dana W.",
  "Chris P.",
  "Nadia H.",
  "Tom B.",
  "Yuki M.",
  "Rachel G.",
  "Omar F.",
];
