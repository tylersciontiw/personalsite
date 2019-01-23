import React from "react"
import { render } from "react-dom"

import HeaderContainer from "./containers/HeaderContainer"


class Header extends React.Component {
  render() {
    return (
      
      <HeaderContainer />
   )
  }
}

render(<Header/>, document.getElementById('Heading'))
