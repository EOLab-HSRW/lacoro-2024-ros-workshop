import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "LACORO 2024 - ROS Workshop",
  description: "LACORO 2024 - ROS Workshop",
  base: "/lacoro-2024-ros-workshop/",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Welcome', link: '/welcome' },
    ],

    sidebar: [
      { text: "Welcome", link: "welcome"},
      { text: "Fundamentals", link: "fundamentals"},
      {
        text: 'Session 1',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
        ]
      },
      {
        text: 'For Instructors',
        items: [
            { text: 'Setup Environment', link: '/instructors/environment'}
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/EOLab-HSRW/lacoro-2024-ros-workshop' },
      { icon: 'linkedin', link:  'https://www.linkedin.com/showcase/earth-observation-lab/'},
      { icon: 'pinboard', link: 'https://www.eolab.de/'}
    ]
  }
})
