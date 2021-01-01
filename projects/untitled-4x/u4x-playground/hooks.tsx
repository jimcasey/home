import { useState, useEffect } from 'react'

export const useWindowSize = () => {
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  })

  useEffect(() => {
    const onResize = () => {
      const { innerWidth: width, innerHeight: height } = window
      setWindowSize({ width, height })
    }
    onResize()

    window.addEventListener('resize', onResize)
    return () => window.removeEventListener('resize', onResize)
  }, [])

  return windowSize
}
