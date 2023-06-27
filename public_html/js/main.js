

  function decrement(e) {
    const btn = e.target.parentNode.parentElement.querySelector(
      'button[data-action="decrement"]'
    );
    const target = btn.nextElementSibling;
    let value = Number(target.value);
    if (value > 1) {
      value--;
      target.value = value;
    }
  }
  
  function increment(e) {
    const btn = e.target.parentNode.parentElement.querySelector(
      'button[data-action="decrement"]'
    );
    const target = btn.nextElementSibling;
    let value = Number(target.value);
    if (value < 20) {
      value++;
      target.value = value;
    }
  }
  
  const decrementButtons = document.querySelectorAll(
    `button[data-action="decrement"]`
  );
  
  const incrementButtons = document.querySelectorAll(
    `button[data-action="increment"]`
  );
  
  decrementButtons.forEach((btn) => {
    btn.addEventListener("click", decrement);
  });
  
  incrementButtons.forEach((btn) => {
    btn.addEventListener("click", increment);
  });
  


  

// --------------------------------------------------------------------------


