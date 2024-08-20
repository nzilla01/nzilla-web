//get element varible

const nav_btn = document.getElementById('btn');
const bar1 = document.getElementById('line1');
const bar2 = document.getElementById('line2');
const bar3 = document.getElementById('line3');
const nav_bar =document.getElementById('list')
 

nav_btn.addEventListener('click', function(){
  bar1.classList.toggle('active');
  bar2.classList.toggle('close');
  bar3.classList.toggle('open');
  nav_bar.classList.toggle('show')
}
);

