/*
  UFORIA · Salah Kostum! Embed
  Pasang di website mana pun dengan satu baris:

    <script src="https://uforia-qr-puzzle-game.pixanimation-official.workers.dev/embed.js" async></script>

  Game muncul tepat di tempat script itu ditaruh. Opsi lewat atribut:
    data-max-width="440"   lebar maksimal dalam piksel (default 440)
    data-radius="18"       sudut bulat dalam piksel (default 18)
    data-target="#id"      taruh game di elemen tertentu, bukan di posisi script
*/
(function () {
  var me = document.currentScript;
  if (!me) return;
  var base = me.src.replace(/embed\.js(\?.*)?$/, "");
  var maxW = parseInt(me.getAttribute("data-max-width") || "440", 10);
  var radius = parseInt(me.getAttribute("data-radius") || "18", 10);
  var target = me.getAttribute("data-target");

  var box = document.createElement("div");
  box.className = "uforia-game";
  box.style.cssText =
    "position:relative;width:100%;max-width:" + maxW + "px;margin:0 auto;" +
    "aspect-ratio:9/16;min-height:560px;max-height:92vh;border-radius:" + radius + "px;" +
    "overflow:hidden;background:#16133d;box-shadow:0 10px 30px rgba(0,0,0,.25)";

  var f = document.createElement("iframe");
  f.src = base + "index.html?embed=1";
  f.title = "UFORIA · Salah Kostum! mini game";
  f.loading = "lazy";
  f.allow = "autoplay; fullscreen";
  f.setAttribute("allowfullscreen", "");
  f.style.cssText = "position:absolute;inset:0;width:100%;height:100%;border:0;display:block";
  box.appendChild(f);

  var host = target && document.querySelector(target);
  if (host) host.appendChild(box);
  else me.parentNode.insertBefore(box, me);
})();
