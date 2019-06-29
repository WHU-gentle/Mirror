var messageBox = document.querySelector('.js-message');
  var btn = document.querySelector('.js-message-btn');
  var card = document.querySelector('.js-profile-card');
  var closeBtn = document.querySelectorAll('.js-message-close');
  var returnBtn = document.querySelector('.js-return');

  btn.addEventListener('click',function (e) {
      window.location.replace("../logout")
  });

  closeBtn.forEach(function (element, index) {
     console.log(element);
      element.addEventListener('click',function (e) {
          e.preventDefault();
          card.classList.remove('active');
      });
  });

  returnBtn.addEventListener('click',function (e) {
      e.preventDefault();
      window.location.replace("../") ;
  });
