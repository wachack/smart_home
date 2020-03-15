/**
 * @file The script copies bundle.js and bundle.css into the static folder of the SmartHome app.
 * @author marcinooo
 */
const path = require('path');
const fs = require('fs');


srcCSS = path.join('bundles', 'bundle.css');
srcJS = path.join('bundles', 'bundle.js');
destCSS = path.join('..', 'smart_home', 'static', 'bundle.css')
destJS = path.join('..', 'smart_home', 'static', 'bundle.js')

// Copy bundle.css
fs.copyFile(srcCSS, destCSS, (err) => {
    if (err) throw err;
    console.log('bundle.css was copied to "' + destCSS + '"');
});

// Copy bundle.js
fs.copyFile(srcJS, destJS, (err) => {
    if (err) throw err;
    console.log('bundle.js was copied to "' + destJS + '"');
});
