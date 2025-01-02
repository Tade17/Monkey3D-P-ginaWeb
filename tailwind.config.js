/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.{html,js}", // Archivos en la raíz
    "./html/**/*.{html,js}", // Archivos en la carpeta html
    "./templates/**/*.{html,js}" // Archivos en la carpeta templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};