module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        nicegray: {
          light: '#2f2f2f',
          DEFAULT: '#1a1a1a',
          dark: '#000'
        }
      }
    },
  },
  variants: {
    extend: {
      textOverflow: ['hover'],
      borderWidth: ['hover', 'focus'],
      width: ['hover']
    },
  },
  plugins: [],
}
