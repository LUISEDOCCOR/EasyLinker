/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/*.html",
    "./src/templates/*/*.html"
  ],
  theme: {
    extend: {
      colors:{
        pastelGreen: "#B5D2AD",
        pastelPink: "#FCDFFF",
        pastelOrange: "#F8D6B3",
        pastelBlue: "#DAF5F0",
        pastelYellow: "#FFFF00",
        neonRed: "#ff4911",

      },
    },
  },
  plugins: [],
}

