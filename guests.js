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
  "backgrounds/01-frost-cream.png",
  "backgrounds/02-alpine-dusk.png",
  "backgrounds/03-snowfall-ivory.png",
  "backgrounds/04-glacier-slate.png",
  "backgrounds/05-powder-linen.png",
  "backgrounds/06-pine-mist.png",
  "backgrounds/07-dawn-summit.png",
  "backgrounds/08-indigo-drift.png",
  "backgrounds/09-birch-blue.png",
  "backgrounds/10-cobalt-cream.png",
  "backgrounds/11-stonewash-oat.png",
  "backgrounds/12-midnight-flurry.png",
];

/* One line per person. Just the name is enough.
   Tip: first name + last initial keeps the page a bit more private,
   since anyone with the link can read it.

   Want to hand-pick someone's image instead of letting it
   auto-assign? Write that line like this:
     { name: "Priya S.", background: "backgrounds/06-lilac-blush.png" },
*/
const GUESTS = [
  // Jess gets the skiing one, pinned so it never gets handed to anyone else.
  // Upload that file to backgrounds/ as jess-skiing.png and this lights up.
  { name: "Jess", background: "backgrounds/jess-skiing.png" },

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
