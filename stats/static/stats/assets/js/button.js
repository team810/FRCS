let duration = 1600,
success = button => {
  //Success function
  button.classList.add('success');
};

document.querySelectorAll('.button-hold').forEach(button => {
  button.style.setProperty('--duration', duration + 'ms');
  ['mousedown', 'touchstart'].forEach(e => {
    button.addEventListener(e, () => {
      button.classList.add('process');
      button.timeout = setTimeout(success, duration, button);
    });
  });
  ['mouseup', 'mouseout', 'touchend'].forEach(e => {
    button.addEventListener(e, () => {
      button.classList.remove('process');
      clearTimeout(button.timeout);
    }, false);
  });
});