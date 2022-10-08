import { createContext, useContext, useState } from 'react'

const DataContext = createContext(null)
const DataDispatchContext = createContext(null)

const DataProvider = ({ children }) => {
  const [data, dispatch] = useState(null)

  return (
    <DataContext.Provider value={data}>
      <DataDispatchContext.Provider value={dispatch}>{children}</DataDispatchContext.Provider>
    </DataContext.Provider>
  )
}

const useData = () => useContext(DataContext)

const useDataDispatch = () => useContext(DataDispatchContext)

export { DataProvider, useData, useDataDispatch }
