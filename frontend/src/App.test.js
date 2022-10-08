import { render, screen } from '@testing-library/react'
import App from './App'

test('renders page', () => {
  render(<App />)
  const element = screen.getByText(/Shrinking that link of yours/i)
  expect(element).toBeInTheDocument()
})
