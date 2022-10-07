import { createContext, useContext, useState } from 'react'

const HashContext = createContext(null)
const HashDispatchContext = createContext(null)

const HashProvider = ({ children }) => {
  const [hash, dispatch] = useState(null)

  return (
    <HashContext.Provider value={hash}>
      <HashDispatchContext.Provider value={dispatch}>{children}</HashDispatchContext.Provider>
    </HashContext.Provider>
  )
}

const useHash = () => useContext(HashContext)

const useHashDispatch = () => useContext(HashDispatchContext)

export { HashProvider, useHash, useHashDispatch }
