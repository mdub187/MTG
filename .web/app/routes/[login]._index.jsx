import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Container as RadixThemesContainer,DropdownMenu as RadixThemesDropdownMenu,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Link as RadixThemesLink,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {Link as ReactRouterLink} from "react-router"
import {ChevronDown as LucideChevronDown,Menu as LucideMenu} from "lucide-react"
import {Root as RadixFormRoot} from "@radix-ui/react-form"
import {EventLoopContext} from "$/utils/context"
import {ReflexEvent,getRefValue,getRefValues} from "$/utils/state"
import {jsx} from "@emotion/react"




function Root_1c2892ca40cc93c088561d3ff381cca3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

    const handleSubmit_ee90fb484b7ae4621ea8d9ebbe10980f = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => null), ["callback"] : null }), ({ ["preventDefault"] : true })))], args, ({  }))))(ev));

        if (false) {
            $form.reset()
        }
    })
    


  return (
    jsx(RadixFormRoot,{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_ee90fb484b7ae4621ea8d9ebbe10980f},jsx(RadixThemesTextField.Root,{name:"username",placeholder:"Username"},),jsx(RadixThemesTextField.Root,{name:"password",placeholder:"Password",type:"password"},),jsx(RadixThemesButton,{type:"submit"},"Login"))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesBox,{css:({ ["background"] : "var(--accent-3)", ["padding"] : "1em", ["width"] : "100%" })},jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2.25em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"7",weight:"bold"},"Reflex")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",justify:"end",gap:"5"},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Home"))),jsx(RadixThemesDropdownMenu.Root,{},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(RadixThemesButton,{css:({ ["weight"] : "medium" }),size:"3",variant:"ghost"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Services"),jsx(LucideChevronDown,{},))),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Pricing"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Contact")))))),jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"6",weight:"bold"},"Reflex")),jsx(RadixThemesDropdownMenu.Root,{css:({ ["justify"] : "end" })},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(LucideMenu,{size:30},)),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Home"),jsx(RadixThemesDropdownMenu.Sub,{},jsx(RadixThemesDropdownMenu.SubTrigger,{},"Services"),jsx(RadixThemesDropdownMenu.SubContent,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesDropdownMenu.Item,{},"About"),jsx(RadixThemesDropdownMenu.Item,{},"Pricing"),jsx(RadixThemesDropdownMenu.Item,{},"Contact")))))),jsx(Root_1c2892ca40cc93c088561d3ff381cca3,{},)),jsx("title",{},"MtgSorterReflex | Login"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}