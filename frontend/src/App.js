import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Shrink from './components/layouts/Shrink'
import './App.css'

function App() {
  return (
    <Router basename="/">
      <Routes>
        <Route path="/" exact element={<Shrink />} />
      </Routes>
    </Router>
  )
}

export default App
