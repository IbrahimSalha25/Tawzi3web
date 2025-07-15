import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Authenticate and connect to Google Sheets
def connect_to_gsheet(creds_json, spreadsheet_name, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name


# Google Sheet credentials and details
SPREADSHEET_NAME = 'Tawzi3 Requests 2025'
SHEET_NAME = 'sheet1'
CREDENTIALS_FILE = 'tawzi3googlesheetname.json'

# Connect to the Google Sheet
sheet_by_name = connect_to_gsheet(CREDENTIALS_FILE, SPREADSHEET_NAME, sheet_name=SHEET_NAME)


def read_data():
    data = sheet_by_name.get_all_records()  # Get all records from Google Sheet
    return pd.DataFrame(data)


# Add Data to Google Sheets
def add_data(row):
    sheet_by_name.append_row(row)  # Append the row to the Google Sheet


st.set_page_config(
    page_title="Tawzi3 - نظام توزيع",
    page_icon="assets/images/icon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تطبيق اتجاه الصفحة من اليمين لليسار (RTL) باستخدام CSS بسيط
st.markdown("""
<style>
    /* تطبيق الخط والاتجاه على كامل التطبيق */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    html, body, [class*="st-"],h1{
        direction: rtl;
        font-family: 'Tajawal', sans-serif;
    }
</style>
""", unsafe_allow_html=True)


def show_main_section():
    st.info("""
    نحن فريق مستقل من غزة، نؤمن بقوة التكنولوجيا في تحسين حياة الناس. 
    قمنا بتطوير نظام **"توزيع"** لمساعدة المؤسسات الإنسانية والجهات المانحة على إدارة وتوزيع المساعدات بكرامة وسهولة.
    """)

    st.markdown("#### 📊 نتائج مثبتة في لمحة")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="🚀 سرعة التسليم", value="5 ثوانٍ", delta="للعملية الواحدة", delta_color="off")
    col2.metric(label="🔒 أمان البيانات", value="100%", delta="بيانات محلية ومشفرة", delta_color="off")
    col3.metric(label="🎯 دقة التوزيع", value="0 تكرار", delta="منع الازدواجية تلقائياً", delta_color="off")
    col4.metric(label="👥 سعة غير محدودة", value="∞", delta="للمستفيدين والبيانات", delta_color="off")


def show_features_section():
    """يعرض قسم مميزات النظام"""
    st.markdown("""
    <h1 style='font-family: Tajawal; color: #333;'>🚀 مميزات نظام \"توزيع\"</h1>
    <h3 style='font-family: Tajawal; color: #555;'>أدوات قوية مصممة خصيصاً لتلبية احتياجاتكم على الأرض.</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### 📷 مسح سريع عبر QR Code")
            st.markdown("""
            - **توليد تلقائي:** إنشاء رمز QR فريد لكل مستفيد.
            - **تسليم فوري:** مسح الرمز بكاميرا اللابتوب لتسجيل عملية التسليم في أقل من 5 ثوانٍ.
            - **تقليل الأخطاء:** ضمان تسليم المساعدة للشخص الصحيح بكل سهولة.
            """)

        with st.container(border=True):
            st.markdown("#### 📊 تقارير ذكية وتصدير فوري")
            st.markdown("""
            - **تقارير شاملة:** عرض إحصائيات دقيقة حول أعداد المستفيدين والمساعدات الموزعة.
            - **تصدير بضغطة زر:** تصدير كافة البيانات إلى ملف Excel لمشاركتها مع الجهات المانحة.
            - **شفافية كاملة:** توفير بيانات موثوقة تدعم اتخاذ القرار.
            """)
        st.image("assets/images/example01.png", use_container_width=True)
    with col2:
        with st.container(border=True):
            st.markdown("#### 🔒 يعمل بدون إنترنت (Offline)")
            st.markdown("""
            - **استمرارية العمل:** النظام يعمل بشكل كامل على جهازك دون الحاجة لأي اتصال بالإنترنت.
            - **أمان مطلق:** جميع بيانات المستفيدين محفوظة محلياً على جهازك فقط.
            - **مثالي للميدان:** مصمم للعمل في الظروف الصعبة التي يندر فيها الاتصال بالشبكة.
            """)

        with st.container(border=True):
            st.markdown("#### ⚙️ واجهة سهلة باللغة العربية")
            st.markdown("""
            - **بساطة الاستخدام:** واجهة مصممة بعناية لتكون سهلة ومباشرة.
            - **دعم كامل للعربية:** جميع القوائم والنماذج تدعم اللغة العربية بشكل كامل.
            - **لا حاجة لتدريب:** يمكن لأي شخص البدء باستخدامه خلال دقائق.
            """)
        st.image("assets/images/example02.png", use_container_width=True)

    st.success("💡 **ميزة الـ QR Code:** هي الميزة الأهم التي تضمن سرعة التوزيع ومنع التكرار نهائياً.")


def show_benefits_section():
    """يعرض قسم الفوائد والجهات المستهدفة"""
    st.header("🌍 لمن هذا النظام؟ وكيف يخدم المجتمع؟")
    st.markdown("أداة واحدة تخدم كافة أطراف العمل الإنساني.")

    st.markdown("##### الجهات المستفيدة")
    col1, col2 = st.columns(2)
    with col1:
        st.success("🏛️ **المؤسسات والجمعيات الخيرية:** لتنظيم قوائم المستفيدين وضمان التوزيع العادل.")
        st.warning("🤝 **المبادرات الشبابية والتطوعية:** للحصول على أداة بسيطة ومجانية تسهل عملهم الميداني.")
    with col2:
        st.info("💰 **الجهات المانحة والمنظمات الدولية:** لمتابعة دقيقة وشفافة لسير عملية توزيع المساعدات.")
        st.error("🏢 **المؤسسات الحكومية وهيئات الطوارئ:** لإدارة بيانات المتضررين في الأزمات بسرعة وفعالية.")

    st.markdown("##### الأثر الإيجابي على المجتمع")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<h3 style='text-align: center;'>⚖️</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><strong>تحقيق العدالة</strong></p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='text-align: center;'>🤝</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><strong>حفظ الكرامة</strong></p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<h3 style='text-align: center;'>⏱️</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><strong>توفير الوقت</strong></p>", unsafe_allow_html=True)
    with col4:
        st.markdown("<h3 style='text-align: center;'>📈</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><strong>زيادة الثقة</strong></p>", unsafe_allow_html=True)


def show_demo_section():
    """يعرض قسم العرض التوضيحي التفاعلي"""
    st.header("🖥️ عرض توضيحي حي")
    st.markdown("تفاعل مع واجهة مبسطة تحاكي النظام الحقيقي.")

    tab1, tab2, tab3 = st.tabs(["➕ **إضافة مستفيد**", "📊 **التقرير**", "📈 **لوحة التحكم**"])

    with tab1:
        st.markdown("##### نموذج إضافة مستفيد جديد")
        with st.form("add_beneficiary_form", border=False):
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("الاسم الكامل", placeholder="مثال: محمد أحمد علي")
                st.text_input("رقم الهوية", placeholder="رقم فريد لتمييز المستفيد")
                st.number_input("عدد أفراد الأسرة", min_value=1, value=5)
            with col2:
                st.selectbox("نوع المساعدة", ["طرد غذائي", "مساعدة نقدية", "ملابس", "أدوية"])
                st.selectbox("الأولوية", ["عادية", "متوسطة", "عالية", "طارئة"])
                st.text_input("رقم الهاتف (اختياري)")

            st.text_area("العنوان", placeholder="المدينة - الحي - أقرب معلم")

            if st.form_submit_button("✅ إضافة المستفيد", use_container_width=True):
                st.success("تمت إضافة المستفيد بنجاح! سيتم توليد رمز QR له تلقائياً.")

    with tab2:
        st.markdown("##### تقرير التوزيع (مثال)")
        report_data = pd.DataFrame({
            'اسم المستفيد': ['أحمد محمد', 'فاطمة علي', 'خالد يوسف', 'سارة محمود'],
            'رقم الهوية': ['123456789', '987654321', '456789123', '789123456'],
            'نوع المساعدة': ['طرد غذائي', 'ملابس', 'مساعدة نقدية', 'طرد غذائي'],
            'تاريخ التسليم': ['2024-07-10', '2024-07-11', '2024-07-12', '2024-07-13'],
        })
        st.dataframe(report_data, use_container_width=True)

        csv = report_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 تصدير التقرير (Excel)",
            data=csv,
            file_name='tawzi3_report_demo.csv',
            mime='text/csv',
            use_container_width=True
        )

    with tab3:
        st.markdown("##### لوحة التحكم الرئيسية (مثال)")
        col1, col2, col3 = st.columns(3)
        col1.metric("إجمالي المستفيدين", "1,250")
        col2.metric("المساعدات الموزعة", "890")
        col3.metric("المساعدات المتبقية", "360")

        chart_data = pd.DataFrame({
            'الفئة': ["المساعدات الموزعة", "المساعدات المتبقية"],
            'العدد': [890, 360],
        })

        # السطر الذي تم تعديله هنا
        st.bar_chart(chart_data, x='الفئة', y='العدد')


def show_contact_section():
    """يعرض قسم التواصل وطلب النسخة"""
    st.markdown("""
    <h2 style='font-family: Tajawal; color: #333;'>📞 تواصل معنا</h1>
    <h4 style='font-family: Tajawal; color: #333;'>نحن هنا للإجابة على استفساراتكم ومساعدتكم.</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📥 اطلب نسختك التجريبية المجانية")

        with st.form("trial_request"):
            organization = st.text_input("اسم المؤسسة", placeholder="اسم المؤسسة أو الجمعية")
            contact_name = st.text_input("اسم المسؤول", placeholder="اسم الشخص المسؤول")
            email = st.text_input("البريد الإلكتروني", placeholder="email@example.com")
            phone = st.text_input("رقم الهاتف", placeholder="+972-XXX-XXXXXX")

            org_type = st.selectbox("نوع المؤسسة", [
                "جمعية خيرية", "مؤسسة حكومية", "مبادرة شبابية",
                "منظمة دولية", "مؤسسة خاصة", "أخرى"
            ])

            beneficiaries = st.number_input("عدد المستفيدين المتوقع", min_value=1, max_value=100000, value=100)

            message = st.text_area("رسالة إضافية", placeholder="أخبرنا عن احتياجاتك...")

            submitted = st.form_submit_button("طلب النسخة التجريبية", use_container_width=True)

            if submitted:
                add_data([organization, contact_name, email, phone, org_type, beneficiaries, message])
                st.success("شكراً لك! تم استلام طلبك بنجاح. سنتواصل معك في أقرب فرصة.")
                st.balloons()

    with col2:
        st.markdown("""
        <div class="form-container">
            <h3>📧 معلومات التواصل</h3>
            <p><strong>📧 البريد الإلكتروني:</strong> tawzi3.app@gmail.com</p>
            <p><strong>📱 واتساب:</strong> +972-XXX-XXXXXX</p>
            <p><strong>📍 الموقع:</strong> غزة - فلسطين</p>
            <p><strong>🌐 وسائل التواصل:</strong></p>
            <p>• فيسبوك: /Tawzi3App</p>
            <p>• تليجرام: @Tawzi3App</p>
        </div>
        """, unsafe_allow_html=True)


# App
st.logo(r"assets/images/logo.png", size="large")
st.markdown("""
<h1 style='font-family: Tajawal; color: #333;'>Tawzi3 - نظام توزيع</h1>
<h3 style='font-family: Tajawal; color: #555;'>نظام ذكي لتوزيع المساعدات بسرعة ودقة عبر تقنية QR</h3>
""", unsafe_allow_html=True)

# main section
show_main_section()

st.write("")
st.divider()
st.write("")

# features section
show_features_section()

st.write("")
st.divider()
st.write("")

# benefits section
show_benefits_section()

st.write("")
st.divider()
st.write("")

# contact section
show_contact_section()

st.write("")
st.divider()

# الخاتمة
st.markdown("""
<div style="text-align: center; color: grey;">
    <p>طُوّر بـ ❤️ في غزة - فلسطين</p>
    <p>© 2025 نظام "توزيع" | جميع الحقوق محفوظة</p>
</div>
""", unsafe_allow_html=True)
