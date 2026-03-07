import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Container as RadixThemesContainer,DropdownMenu as RadixThemesDropdownMenu,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Link as RadixThemesLink,Text as RadixThemesText} from "@radix-ui/themes"
import {Link as ReactRouterLink} from "react-router"
import {ChevronDown as LucideChevronDown,Menu as LucideMenu} from "lucide-react"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue} from "$/utils/state"
import {jsx} from "@emotion/react"




function Button_2f50925bae488451206f83454afad555 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);
const reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state)

const on_click_f7ee70994f1c937cfc952cee377e4a59 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.mtg_sorter_reflex___cond___login_buton_display____cond_state.change", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{onClick:on_click_f7ee70994f1c937cfc952cee377e4a59},(reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state.show_rx_state_ ? "Hide" : "Show"))
  )
}


function Fragment_487a3f00c4b09ba162ee37e0b2182819 () {
  const reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state)



  return (
    jsx(Fragment,{},(reflex___state____state__mtg_sorter_reflex___cond___login_buton_display____cond_state.show_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "blue" })},"Login"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "red" })},"Account")))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesBox,{css:({ ["background"] : "var(--accent-3)", ["padding"] : "1em", ["width"] : "100%" })},jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2.25em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"7",weight:"bold"},"Reflex")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",justify:"end",gap:"5"},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Home"))),jsx(RadixThemesDropdownMenu.Root,{},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(RadixThemesButton,{css:({ ["weight"] : "medium" }),size:"3",variant:"ghost"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Services"),jsx(LucideChevronDown,{},))),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Pricing"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Contact")))))),jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"6",weight:"bold"},"Reflex")),jsx(RadixThemesDropdownMenu.Root,{css:({ ["justify"] : "end" })},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(LucideMenu,{size:30},)),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Home"),jsx(RadixThemesDropdownMenu.Sub,{},jsx(RadixThemesDropdownMenu.SubTrigger,{},"Services"),jsx(RadixThemesDropdownMenu.SubContent,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesDropdownMenu.Item,{},"About"),jsx(RadixThemesDropdownMenu.Item,{},"Pricing"),jsx(RadixThemesDropdownMenu.Item,{},"Contact")))))),jsx(RadixThemesHeading,{size:"3"},"Home Page"),jsx(RadixThemesText,{as:"p"},"welcome home"),jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesButton,{},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/upload"},"Upload"))),jsx(RadixThemesButton,{},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/collection"},"Collection"))),jsx(RadixThemesButton,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(Button_2f50925bae488451206f83454afad555,{},),jsx(Fragment_487a3f00c4b09ba162ee37e0b2182819,{},))))),jsx("title",{},"MtgSorterReflex | Home"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}