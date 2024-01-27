function CheckDOM(str) { 
  let stack = []; // pila para almacenar las etiquetas de apertura
  let tags = ["b", "i", "em", "div", "p"]; // etiquetas soportadas
  let almostCorrect = null; // variable para almacenar la etiqueta que podría corregir la cadena

  // iteramos a través de la cadena, buscando etiquetas HTML
  str.replace(/<\/?([a-z]+)>/g, (match, tag) => {
    // si la etiqueta está en la lista de etiquetas soportadas
    if (tags.includes(tag)) {
      // si es una etiqueta de apertura
      if (match[1] !== "/") {
        // la añadimos a la pila
        stack.push(tag);
      } else {
        // si es una etiqueta de cierre
        // si la pila está vacía
        if (stack.length === 0) {
          // si almostCorrect no ha sido establecido, lo establecemos a la etiqueta actual
          // si ya ha sido establecido, lo establecemos a false, indicando que más de una etiqueta necesita ser cambiada
          almostCorrect = almostCorrect === null ? tag : false;
        } else if (stack[stack.length - 1] === tag) {
          // si la etiqueta de cierre coincide con la etiqueta de apertura en la cima de la pila, la sacamos de la pila
          stack.pop();
        } else {
          // si la etiqueta de cierre no coincide con la etiqueta de apertura en la cima de la pila
          // si almostCorrect no ha sido establecido, lo establecemos a la etiqueta en la cima de la pila
          // si ya ha sido establecido, lo establecemos a false, indicando que más de una etiqueta necesita ser cambiada
          almostCorrect = almostCorrect === null ? stack.pop() : false;
        }
      }
    }
  });

  // si la pila está vacía al final, la cadena es correcta o casi correcta
  if (stack.length === 0) {
    // si almostCorrect no ha sido establecido, la cadena es correcta y devolvemos true
    // si almostCorrect ha sido establecido, la cadena es casi correcta y devolvemos la etiqueta que la haría correcta
    return almostCorrect === null ? true : almostCorrect;
  } else {
    // si la pila no está vacía al final, la cadena es incorrecta y devolvemos false
    return false;
  }
}