

let html_elements = document.querySelectorAll("body *:not(script):not(style):not(meta)");

for (const element of html_elements) {
    if (element.innerText) {
        let originalText = element.innerText;
        console.log(element.innerText);
    }
    const translatedText = translateToHindi(originalText);
    element.innerText = translatedText;
}


function translateToHindi(text) {
    // Your logic to translate the text to Hindi
    return translatedText;
}


