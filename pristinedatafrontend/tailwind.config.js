/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'theme': '#285D5E',
        'theme-dark': '#1f4f4f',
      }
    },
  },
  plugins: [],
}

