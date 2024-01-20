function main() {
   addSmoothScrollWhenRedirecting();
   setTimeout(() => addHeaderWritingAnimation('header #header-content h1 span:last-child', ['Black Crows', 'White Soldiers']), 3000);
}


//--- Smooth Scroll
function addSmoothScrollWhenRedirecting() {
   document.querySelectorAll('.smooth-scroll').forEach((anchor) => {
      anchor.addEventListener('click', (e) => {
         e.preventDefault();

         const targetID = anchor.getAttribute('href').substring(1);
         const targetElement = document.getElementById(targetID);

         if(targetElement) {
            window.scrollTo({
               top: targetElement.offsetTop-100,
               behavior: "smooth",
            })
         }
      });
   });
}

//--- Header Animation
function addHeaderWritingAnimation(elQuery, titles, titleIndex = 0) {
   if(typeof titles != 'object') return;

   const el = document.querySelector(elQuery);
   if(!el) return;

   if(titleIndex >= titles.length) titleIndex = 0;

   // delete
   let time = 0;
   for (let i = el.innerText.length; i >= 0; i--) {
      setTimeout(() => {
         el.innerText = el.innerText.slice(0, i);
      }, time);

      time += 100;
   }

   // write
   for (let i = 0; i <= titles[titleIndex].length; i++) {
      setTimeout(() => {
         el.innerText = titles[titleIndex].slice(0, i);
      }, time);

      time += 100;
   }

   // keep animation running
   setTimeout(() => addHeaderWritingAnimation(elQuery, titles, titleIndex + 1), time + 3000);
}

//--- Toggle Navbar Menu
function toggleNavMenu(elQuery) {
   if(typeof elQuery !== 'string') return;

   const el = document.querySelector(elQuery);
   if(!el) return;

   const collapse = () => {
      el.style.height = `${el.scrollHeight}px`;
      el.offsetHeight;
      el.classList.add('collapsing');
      el.style.height = ``;

      setTimeout(() => {
         el.classList.remove('collapsing');
         el.classList.toggle('show');
      }, 350);
   };

   const show = () => {
      el.classList.add('collapsing');
      el.classList.toggle('show');
      el.style.height = `${el.scrollHeight}px`;

      setTimeout(() => {
         el.classList.remove('collapsing');
         el.style.height = ``;
      }, 350);
   };

   if(el.classList.contains('collapsing')) return;
   if(el.classList.contains('show')) collapse();
   else show();
}

document.addEventListener("DOMContentLoaded", function() {
   main();
});