import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { DataProvider } from './Contexts.js'
import Shrink from './components/layouts/Shrink'
import Result from './components/layouts/Result'
import './App.css'

function App() {
  const basename = process.env.PUBLIC_URL

  return (
    <DataProvider>
      <Router basename={basename}>
        <Routes>
          <Route path="/" exact element={<Shrink />} />
          <Route path="/result/" element={<Result />} />
        </Routes>
      </Router>
    </DataProvider>
  )
}

export default App
