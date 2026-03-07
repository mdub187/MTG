import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Container as RadixThemesContainer,DropdownMenu as RadixThemesDropdownMenu,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Link as RadixThemesLink,Separator as RadixThemesSeparator,Spinner as RadixThemesSpinner,Table as RadixThemesTable,Text as RadixThemesText} from "@radix-ui/themes"
import {Link as ReactRouterLink} from "react-router"
import {ChevronDown as LucideChevronDown,Menu as LucideMenu} from "lucide-react"
import {} from "react-dropzone"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue,refs} from "$/utils/state"
import {useDropzone} from "react-dropzone"
import {jsx} from "@emotion/react"




function Comp_c994754fcf04888833154247b80cb25b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_drop_62cb2352434346f8abdd3c6e280a35bb = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.mtg_sorter_reflex___state___ocr_state.handle_upload", ({ ["files"] : _ev_0, ["upload_id"] : "default", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((osizayzf) => (osizayzf?.["file"]?.["path"]+": "+osizayzf?.["errors"].map(((wnkiegyk) => wnkiegyk?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: xdvxrcsn, getInputProps: udaxihhe, isDragActive: bacghqta} = useDropzone(({ ["accept"] : ({ ["image/jpeg"] : [".jpg", ".jpeg"], ["image/png"] : [".png"] }), ["multiple"] : true, ["maxFiles"] : 20, ["onDrop"] : on_drop_62cb2352434346f8abdd3c6e280a35bb, ["id"] : "default", ["onDropRejected"] : on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 }));



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["border"] : "1px dashed gray", ["padding"] : "2em", ["borderRadius"] : "md", ["width"] : "100%", ["textAlign"] : "center" }),...xdvxrcsn()},jsx("input",{type:"file",...udaxihhe()},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p"},"Drag and drop images here or click to browse"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray" }),size:"6"},"Supports: JPG, PNG"))))
  )
}


function Button_9317ec6d7f044864d82838111cac0446 () {
  const reflex___state____state__mtg_sorter_reflex___state___ocr_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___state___ocr_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_4d6c4857362cfe630936bc4c68bf283f = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.mtg_sorter_reflex___state___ocr_state.process_images", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["isLoading"] : reflex___state____state__mtg_sorter_reflex___state___ocr_state.is_processing_rx_state_, ["isDisabled"] : (isTrue(reflex___state____state__mtg_sorter_reflex___state___ocr_state.uploaded_files_rx_state_) ? false : true) }),onClick:on_click_4d6c4857362cfe630936bc4c68bf283f},"Process Images")
  )
}


function Button_04639bb33a78f3b5412ffb0befc1091a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_604be3958bcf65a088c630f598511f54 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.mtg_sorter_reflex___state___ocr_state.clear_results", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{onClick:on_click_604be3958bcf65a088c630f598511f54,variant:"outline"},"Clear")
  )
}


function Table__body_c638948a154d1fedc5d16e216e211340 () {
  const reflex___state____state__mtg_sorter_reflex___state___ocr_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___state___ocr_state)



  return (
    jsx(RadixThemesTable.Body,{},Array.prototype.map.call(reflex___state____state__mtg_sorter_reflex___state___ocr_state.results_rx_state_ ?? [],((result_rx_state_,index_128629ad6118eaa321878098392ad0b0)=>(jsx(RadixThemesTable.Row,{key:index_128629ad6118eaa321878098392ad0b0},jsx(RadixThemesTable.Cell,{},result_rx_state_?.["file"]),jsx(RadixThemesTable.Cell,{},result_rx_state_?.["name"]),jsx(RadixThemesTable.Cell,{},result_rx_state_?.["set"]),jsx(RadixThemesTable.Cell,{},result_rx_state_?.["color"]),jsx(RadixThemesTable.Cell,{},("$"+result_rx_state_?.["price"])),jsx(RadixThemesTable.Cell,{},result_rx_state_?.["rarity"]))))))
  )
}


function Button_6c239850e7d16280386998b9ed6fe52c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_6fe07bf46ddee352922814258498dc0a = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.mtg_sorter_reflex___state___ocr_state.export_to_csv", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["marginTop"] : 3, ["width"] : "100%" }),onClick:on_click_6fe07bf46ddee352922814258498dc0a},"Export to CSV")
  )
}


function Fragment_613bb519990d8ae645aea68added7a26 () {
  const reflex___state____state__mtg_sorter_reflex___state___ocr_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___state___ocr_state)



  return (
    jsx(Fragment,{},(isTrue(reflex___state____state__mtg_sorter_reflex___state___ocr_state.results_rx_state_)?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesTable.Root,{},jsx(RadixThemesTable.Header,{},jsx(RadixThemesTable.Row,{},jsx(RadixThemesTable.ColumnHeaderCell,{},"File"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Card Name"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Set"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Color"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Price"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Rarity"))),jsx(Table__body_c638948a154d1fedc5d16e216e211340,{},)),jsx(Button_6c239850e7d16280386998b9ed6fe52c,{},)))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.500", ["textAlign"] : "center", ["padding"] : "2em" })},"No results yet. Upload and process images to see results.")))))
  )
}


function Fragment_0f3c1bb8b33a7fa65a7607e9fcdbed04 () {
  const reflex___state____state__mtg_sorter_reflex___state___ocr_state = useContext(StateContexts.reflex___state____state__mtg_sorter_reflex___state___ocr_state)



  return (
    jsx(Fragment,{},(reflex___state____state__mtg_sorter_reflex___state___ocr_state.is_processing_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "2em" })},jsx(RadixThemesSpinner,{},)))):(jsx(Fragment_613bb519990d8ae645aea68added7a26,{},))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesBox,{},jsx(RadixThemesBox,{css:({ ["background"] : "var(--accent-3)", ["padding"] : "1em", ["width"] : "100%" })},jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2.25em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"7",weight:"bold"},"Reflex")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",justify:"end",gap:"5"},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Home"))),jsx(RadixThemesDropdownMenu.Root,{},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(RadixThemesButton,{css:({ ["weight"] : "medium" }),size:"3",variant:"ghost"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Services"),jsx(LucideChevronDown,{},))),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Pricing"))),jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{to:"/#"},jsx(RadixThemesText,{as:"p",size:"4",weight:"medium"},"Contact")))))),jsx(RadixThemesBox,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "2em", ["height"] : "auto", ["borderRadius"] : "25%" }),src:"/logo.jpg"},),jsx(RadixThemesHeading,{size:"6",weight:"bold"},"Reflex")),jsx(RadixThemesDropdownMenu.Root,{css:({ ["justify"] : "end" })},jsx(RadixThemesDropdownMenu.Trigger,{},jsx(LucideMenu,{size:30},)),jsx(RadixThemesDropdownMenu.Content,{},jsx(RadixThemesDropdownMenu.Item,{},"Home"),jsx(RadixThemesDropdownMenu.Sub,{},jsx(RadixThemesDropdownMenu.SubTrigger,{},"Services"),jsx(RadixThemesDropdownMenu.SubContent,{},jsx(RadixThemesDropdownMenu.Item,{},"Service 1"),jsx(RadixThemesDropdownMenu.Item,{},"Service 2"),jsx(RadixThemesDropdownMenu.Item,{},"Service 3"))),jsx(RadixThemesDropdownMenu.Item,{},"About"),jsx(RadixThemesDropdownMenu.Item,{},"Pricing"),jsx(RadixThemesDropdownMenu.Item,{},"Contact"))))))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "2em" }),direction:"column",gap:"3"},jsx(RadixThemesHeading,{css:({ ["marginBottom"] : 3 }),size:"5"},"MTG Card Sorter"),jsx(RadixThemesBox,{},),jsx(RadixThemesBox,{css:({ ["width"] : "100%" })},jsx(Comp_c994754fcf04888833154247b80cb25b,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["marginTop"] : 3 }),direction:"row",gap:"3"},jsx(Button_9317ec6d7f044864d82838111cac0446,{},),jsx(Button_04639bb33a78f3b5412ffb0befc1091a,{},)),jsx(RadixThemesSeparator,{css:({ ["marginTop"] : "1em", ["marginBottom"] : "1em" }),size:"4"},),jsx(RadixThemesHeading,{css:({ ["marginBottom"] : 3 }),size:"5"},"Results"),jsx(Fragment_0f3c1bb8b33a7fa65a7607e9fcdbed04,{},))),jsx("title",{},"MtgSorterReflex | Upload"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}