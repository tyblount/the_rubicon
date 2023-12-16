import streamlit as st
import pandas as pd

boys = ['Kobe', 'Trevarius', 'Judah', 'Jordy', 'Samson', 'Brady', 'James', 'Dylan', 'Chef', 'David', 'Drew', 'Toly', 'Olive', 'Lucas', 'Bryan', 'Andy']

overview = """Hey what's up!? It's Ty, and I'm inviting you to join me on an absolute banger of a trip! Set on the stunning Rubicon River, we’ll spend three nights wrapped around a weekend in late June/early July in untamed wilderness. But this trip isn't just backpacking; it’s an opportunity to celebrate Jesus and friendship, all while immersing ourselves in the natural beauty of God’s creation.

Our journey will begin at my grandparents’ on day zero. We’ll kick off at 5:30 pm, allowing us to unwind in the hot tub, catch up a bit, make some friends, double check our gear, share a hearty dinner, and gather around a campfire for a brief talk about the adventure that lies ahead. We'll head out the next morning, and as we traverse the rugged beauty of the Rubicon, we’ll forge bonds and strengthen friendships. On the morning of our last day, we’ll hike out, eat lunch at In-N-Out, then head to my grandparents for a final soak in the hot tub. Expect a group chat about a month prior to the excursion, ensuring everyone is well-prepared and eager for the trip.

This is an opportunity to share in conversations on faith, Jesus, and youth ministry in a setting that encourages both exploration and spiritual introspection. I would love for you to come, and if you want to but are concerned about travel arrangements, splitting gas costs, or other logistical issues, we will make it work, just reach out to me at (530)615-9619! Trying to keep it a tight group. Some people you know may have not been invited, so let's keep it lowkey.

Will you join me?"""

gear_necessities = ['Backpacking backpack', 'Sleeping bag', 'Sleeping pad/Hammock', 'Headlamp/Flashlight', 'Waterbottle', 'Swim trunks', 'Comfortable shoes']

gear_suggestions = ['Comfortable water shoes', 'Sunshirt/Athletic shirt', 'Wet suit top (1.5mm should do)', 'Fishing gear (must have a license, let me know if you are interested)', 'Cooking gear', 'Swim goggles', 'Floaty of some sort (think river rat, lifevest, or something more funky)']

input_name = st.text_input("What's your name? (hint: check postage)")

if input_name in boys:
    st.title('T H E   R U B I C O N')  # title

    tab1, tab2, tab3 = st.tabs(['Overview', 'Gear', 'Are you in?'])  # create tabs with info
    tab1.write(overview) # prints paragraphs in tab 1
    
    tab2.write("Some of you have been backpacking in similar climates and environments and some haven't been backpacking at all! I've put together a couple lists of gear that you'll need and gear I recommend. Take a look:)")
    with tab2: # in tab 2, this fills in below the written line given above 2 columns, one with essential gear and another with recommended gear
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('ESSENTIAL:')
        for gear in gear_necessities:
            col1.write(gear)
        with col2:
            st.subheader('SUGGESTIONS:')
        for gear in gear_suggestions:
            col2.write(gear)
    
    with tab3: # insertion of a google form using st.markdown
        html_code = '<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdwq2B_OvJp1lpkRtzkDw2keT7n6mpuddhkOPIqbbCYphgC4A/viewform?embedded=true" width="640" height="2083" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>'

        st.markdown(html_code, unsafe_allow_html=True)

#    tab4.write('try to embed media on this page, or maybe this is a good one to stick in the sidebar. Difficult to tell but need to tailor to a mobile environment.') # this was going to be an extra tab but I think it'll take a bit to actually fill out. probs have it done and ready by the groupchat and send it out then.

elif input_name == "": #catching an exception if nothing is input for the name
    print("")

else: #meager way to catch if you input the incorrect name.
    st.write('You are not on the list ' + input_name + '.')
    st.stop()
