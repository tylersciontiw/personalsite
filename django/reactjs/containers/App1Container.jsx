import React from "react"
import Radium from "radium"

import { connect } from "react-redux"

import Headline from "../components/Headline"

@Radium
export default class App1Container extends React.Component {
  render() {
    return (
      <div>
    <div className="Hero">
      <div className="HeroGroup">
        <h1>Hi, I'm Tyler</h1>
        <p>Welcome to my portfolio.<br /> I'm passionate about technology and writing.</p>
        
      </div>
      
    </div>
    <h3 className = "WorkHeader">I work with</h3>
    <div className = "Logos">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1000px-React-icon.svg.png" width="125"/>
        <img src="http://www.stickpng.com/assets/images/5848152fcef1014c0b5e4967.png" width="75"/>
        <img src="https://pngimage.net/wp-content/uploads/2018/05/django-png-9.png" width="150"/>
        </div>
        <h3 className = "WorkHeader">I design with</h3>
        <div className = "Logos">
        <img src="https://www.sketchapp.com/images/pages/press/sketch-press-kit/app-icons/sketch-mac-icon@2x.png" width="75"/>
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Affinity-Designer.png" width="75"/>
        </div>
    <div className="Cards">
    <h2>I write too, here are some samples of my work</h2>
      
    </div>
    
  </div>
    )
  }
}