import streamlit as st
import pandas as pd

boys = ['Kobe', 'Trevarius', 'Judah', 'Jordy', 'Samson', 'Brady', 'James', 'Dylan', 'Chris', 'David', 'Drew', 'Toly']
surveyQ = ['Best_date', 'Missing gear', 'General_questions', 'Recommendations', 'Expectations', 'Prayer', 'RUIn']
df_survey = pd.DataFrame(index = boys, columns = surveyQ)

overview = """Hey what's up! It's Ty, and I'm inviting you to join me on an absolute banger of a trip! Set on the stunning Rubicon River, we’ll spend four nights, wrapped around a weekend in late June or early July, and delve into untamed wilderness, creating memories that will last a lifetime. This trip is not just about backpacking; it’s an opportunity to celebrate Jesus and friendship, all while immersing ourselves in the natural beauty of God’s creation.

Our journey will begin at my grandparents’ on, say, a Thursday night. We’ll kick off at 5:30 pm, allowing us to unwind in the hot tub, catch up a bit, make some friends, double check our gear, share a hearty dinner, and gather around a campfire for a brief talk about the adventure that lies ahead. Friday morning we’ll embark, and as we traverse the rugged beauty of the Rubicon, we’ll forge bonds and strengthen friendships. Monday morning we’ll hike out and lunch at In-N-Out, then head to my grandparents for a final soak in the hot tub. Expect a group chat about a month prior to The Radical, ensuring everyone is well-prepared and eager for the trip. It isn’t just about the scenic beauty that surrounds us; it’s an opportunity to share in conversations on faith, Jesus, and youth ministry in a setting that encourages both exploration and spiritual introspection.

If you want to come but are concerned about travel arrangements or other logistical issues, we will make it work.

Will you join me?"""

gear_necessities = ['Backpacking backpack', 'Sleeping bag', 'Sleeping pad/Hammock', 'Headlamp/Flashlight', 'Waterbottle', 'Swim trunks', 'Comfortable shoes']

gear_suggestions = ['Comfortable water shoes', 'Sunshirt/Athletic shirt', 'Wet suit top (1.5mm should do)', 'Fishing gear (must have a license, let me know if you are interested)', 'Cooking gear', 'Swim goggles', 'Floaty of some sort (think river rat, lifevest, or something more funky)']

input_name = st.text_input("What's your name? (hint: check postage)")

if input_name in boys:
    st.title('T H E   R A D I C A L')  # title

    tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Gear', 'Are you in?', 'Media Packet'])  # create tabs with info
    tab1.write(overview)
    
    tab2.write("Some of you have been backpacking in similar climates and environments and some haven't been backpacking! I've put together a couple lists of gear that you'll need and gear I recommend. Take a look:)")
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.write('ESSENTIAL:')
        for gear in gear_necessities:
            col1.write(gear)
        with col2:
            st.write('SUGGESTIONS:')
        for gear in gear_suggestions:
            col2.write(gear)
    
    with tab3:
        best_date = st.radio("Which weekend works best for you?", options = ["July 3-7, Wed-Sun", "July 11-15, Thu-Mon", "Other"])
        if best_date == 'Other':
            best_date = st.text_input("What other weekend(s) work for you:")
        gear_essentials = st.multiselect('Are you missing any essential gear?', options = gear_necessities)
        #if RUIn is 'No':
        #    Not_in = st.text_area("If you don't mind sharing, is there anything I can do to get you on this trip?")
        General_Questions = st.text_area("General questions or concerns about the trip:", value = "")
        Recommendations = st.text_area('Do you have any recommendations for the trip?', value = "")
        Expectations = st.text_area('Is there anything you wish to get out of a trip like this?', value = "")
        Prayer = st.text_area('Do you have any prayer requests?', value = "")
        RUIn = st.radio("Are you in?", options=["Yes", "No"])
        
        # Create a session state to persist data
        if 'session_data' not in st.session_state:
             st.session_state.session_data = {'df_survey': pd.DataFrame(index=boys, columns=surveyQ)}
        
        if st.button('Submit!'):
            st.session_state.session_data['df_survey'].loc[input_name] = [best_date, gear_essentials, General_Questions, Recommendations, Expectations, Prayer, RUIn]
            #df_survey.loc[input_name] = [best_date, gear_essentials, General_Questions, Recommendations, Expectations, Prayer, RUIn]
            st.write('Submitted!')

            st.session_state.session_data['best_date'] = ""
            st.session_state.session_data['gear_essentials'] = ""
            st.session_state.session_data['General_Questions'] = ""
            st.session_state.session_data['Recommendations'] = ""
            st.session_state.session_data['Expectations'] = ""
            st.session_state.session_data['Prayer'] = ""
            st.session_state.session_data['RUIn'] = ""

    if input_name == 'Toly':
        #st.write(df_survey)
        st.write(st.session_state.session_data['df_survey'])

    tab4.write('try to embed media on this page, or maybe this is a good one to stick in the sidebar. Difficult to tell but need to tailor to a mobile environment.')

elif input_name is "":
    print("")

else:
    st.write('You are not on the list, ' + input_name + '.')
    st.stop()
