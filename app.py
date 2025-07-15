import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime
import base64
from io import BytesIO

# إعداد الصفحة
st.set_page_config(
    page_title="Tawzi3 - نظام توزيع المساعدات الذكي",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إعداد الـ CSS المخصص
st.markdown("""
<style>
    /* تحسين الخط العربي */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700&display=swap');

    .main {
        direction: rtl;
        font-family: 'Tajawal', sans-serif;
    }

    /* تحسين العناوين */
    .title-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    /* كارد المميزات */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-right: 4px solid #667eea;
        transition: transform 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    /* أزرار تفاعلية */
    .custom-button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
        margin: 0.5rem;
    }

    .custom-button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    /* إحصائيات */
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }

    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
    }

    .stat-label {
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }

    /* قسم الفوائد */
    .benefits-section {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }

    /* تحسين الشريط الجانبي */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }

    /* تنسيق الأيقونات */
    .icon-large {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    /* تحسين الجداول */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    /* أنيميشن للعناصر */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .animate-fade-in {
        animation: fadeInUp 0.6s ease-out;
    }

    /* تحسين النماذج */
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }

    /* Footer */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
    }

    /* إخفاء العناصر غير المرغوبة */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# الوظائف المساعدة
def create_feature_card(icon, title, description):
    return f"""
    <div class="feature-card animate-fade-in">
        <div style="text-align: center;">
            <div class="icon-large">{icon}</div>
            <h3 style="color: #667eea; margin-bottom: 1rem;">{title}</h3>
            <p style="color: #666; line-height: 1.6;">{description}</p>
        </div>
    </div>
    """


def create_stats_card(number, label, color):
    return f"""
    <div style="background: {color}; padding: 1.5rem; border-radius: 10px; text-align: center; color: white; margin: 0.5rem;">
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """


# الصفحة الرئيسية
def main_page():
    # العنوان الرئيسي
    st.markdown("""
    <div class="title-header animate-fade-in">
        <h1 style="margin: 0; font-size: 3rem;">🟩 برنامج Tawzi3</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.3rem; opacity: 0.9;">نظام توزيع المساعدات الذكي</p>
    </div>
    """, unsafe_allow_html=True)

    # قسم من نحن
    st.markdown("## 💬 من نحن؟")
    st.markdown("""
    <div class="feature-card animate-fade-in">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #444;">
        مرحبًا! نحن فريق مستقل من غزة، نؤمن بأن التقنية قادرة على تحسين حياة الناس. 
        طورنا برنامج <strong>Tawzi3</strong> ليساعد المؤسسات الخيرية والجهات المانحة في 
        <strong>توزيع المساعدات بكرامة وسهولة</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # قسم ما هو Tawzi3
    st.markdown("## 🎯 ما هو Tawzi3؟")
    st.markdown("""
    <div class="feature-card animate-fade-in">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #444;">
        <strong>Tawzi3</strong> هو نظام سطح مكتب ذكي يساعد المؤسسات في تنظيم وتوزيع المساعدات 
        (طرود غذائية، ملابس، مساعدات نقدية...) بشكل منظم، عادل، وسريع، 
        <strong>دون الحاجة لاتصال بالإنترنت</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # إحصائيات مثيرة للإعجاب
    st.markdown("### 📊 نتائج مذهلة")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(create_stats_card("5", "ثوانٍ", "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"),
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; margin-top: 0.5rem;'>لكل عملية توزيع</p>", unsafe_allow_html=True)

    with col2:
        st.markdown(create_stats_card("100%", "أمان", "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"),
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; margin-top: 0.5rem;'>بيانات محلية آمنة</p>", unsafe_allow_html=True)

    with col3:
        st.markdown(create_stats_card("0", "تكرار", "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"),
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; margin-top: 0.5rem;'>منع التكرار تلقائيًا</p>",
                    unsafe_allow_html=True)

    with col4:
        st.markdown(create_stats_card("∞", "سعة", "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)"),
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; margin-top: 0.5rem;'>عدد لا محدود من المستفيدين</p>",
                    unsafe_allow_html=True)


# صفحة المميزات
def features_page():
    st.markdown("## 🚀 مميزات البرنامج")

    # المميزات الرئيسية
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(create_feature_card(
            "📌",
            "تنظيم ذكي لقوائم المستفيدين",
            "• إضافة وتعديل وحذف المستفيدين<br>• تصنيف الحالات حسب الأولوية<br>• منع التكرار تلقائيًا"
        ), unsafe_allow_html=True)

        st.markdown(create_feature_card(
            "📊",
            "تقارير جاهزة وقابلة للتصدير",
            "• إحصائيات شاملة ومفصلة<br>• تصدير Excel بكبسة زر<br>• تقارير تفاعلية"
        ), unsafe_allow_html=True)

        st.markdown(create_feature_card(
            "🖥️",
            "واجهة سهلة وباللغة العربية",
            "• تصميم بسيط وسهل الاستخدام<br>• لا تحتاج تدريب معقد<br>• دعم كامل للغة العربية"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(create_feature_card(
            "📷",
            "استخدام QR لتسريع التوزيع",
            "• توليد كود QR لكل مستفيد<br>• مسح سريع وتسجيل فوري<br>• أقل من 5 ثوانٍ لكل عملية!"
        ), unsafe_allow_html=True)

        st.markdown(create_feature_card(
            "🔒",
            "حماية وأمان",
            "• بيانات محفوظة محليًا<br>• لا إرسال عبر الإنترنت<br>• نسخ احتياطي آمن"
        ), unsafe_allow_html=True)

        # عرض توضيحي للـ QR
        st.markdown("### 📱 مثال على كود QR")
        qr_demo = go.Figure()
        qr_demo.add_trace(go.Scatter(
            x=[0, 1, 1, 0, 0],
            y=[0, 0, 1, 1, 0],
            mode='lines+markers',
            fill='toself',
            fillcolor='rgba(102, 126, 234, 0.1)',
            line=dict(color='rgb(102, 126, 234)', width=2),
            name='QR Code Area'
        ))
        qr_demo.update_layout(
            title="مثال على كود QR للمستفيد",
            showlegend=False,
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(qr_demo, use_container_width=True)


# صفحة الفوائد
def benefits_page():
    st.markdown("## 👥 لمن هذا البرنامج؟")

    target_groups = [
        ("🏛️", "المؤسسات الخيرية والجمعيات", "تنظيم فعال للمساعدات وضمان الوصول العادل"),
        ("🤝", "المبادرات الشبابية التطوعية", "أدوات بسيطة لتسهيل العمل التطوعي"),
        ("💰", "الجهات المانحة", "متابعة دقيقة لتوزيع المساعدات"),
        ("🏢", "المؤسسات الحكومية", "نظام موثوق لحالات الطوارئ")
    ]

    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(target_groups):
        with cols[i % 2]:
            st.markdown(create_feature_card(icon, title, desc), unsafe_allow_html=True)

    st.markdown("## 🌍 كيف يخدم Tawzi3 المجتمع؟")

    st.markdown("""
    <div class="benefits-section animate-fade-in">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                <h4>تسريع العمليات</h4>
                <p>يقلل الطوابير والازدحام المزعج</p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚖️</div>
                <h4>ضمان العدالة</h4>
                <p>يضمن عدالة التوزيع ومنع التكرار</p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🤝</div>
                <h4>تحسين التنسيق</h4>
                <p>يسهل التنسيق بين المؤسسات</p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💪</div>
                <h4>توفير الجهد</h4>
                <p>يوفر وقت وجهد كبير على الجميع</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# صفحة العرض التوضيحي
def demo_page():
    st.markdown("## 📱 العرض التوضيحي")

    # محاكاة واجهة البرنامج
    st.markdown("### 🖥️ واجهة البرنامج")

    tab1, tab2, tab3 = st.tabs(["الصفحة الرئيسية", "إضافة مستفيد", "تقرير"])

    with tab1:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 لوحة التحكم الرئيسية</h4>
            <p>عرض سريع لأهم الإحصائيات والعمليات</p>
        </div>
        """, unsafe_allow_html=True)

        # محاكاة بيانات
        demo_data = {
            'عدد المستفيدين': 1250,
            'المساعدات الموزعة': 890,
            'في الانتظار': 360,
            'التكرارات المحظورة': 15
        }

        cols = st.columns(4)
        colors = ['#667eea', '#f093fb', '#a8edea', '#ffecd2']

        for i, (key, value) in enumerate(demo_data.items()):
            with cols[i]:
                st.metric(key, value)

        # رسم بياني للتوزيع
        fig = go.Figure(data=[
            go.Bar(x=list(demo_data.keys()), y=list(demo_data.values()),
                   marker_color=colors)
        ])
        fig.update_layout(
            title="إحصائيات التوزيع",
            xaxis_title="الفئة",
            yaxis_title="العدد",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("### ➕ إضافة مستفيد جديد")

        with st.form("add_beneficiary"):
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("اسم المستفيد", placeholder="أدخل الاسم الكامل")
                id_number = st.text_input("رقم الهوية", placeholder="رقم الهوية أو الإقامة")
                phone = st.text_input("رقم الهاتف", placeholder="+972-XXX-XXXXXX")

            with col2:
                family_size = st.number_input("عدد أفراد الأسرة", min_value=1, max_value=20, value=5)
                aid_type = st.selectbox("نوع المساعدة", ["طرد غذائي", "ملابس", "مساعدة نقدية", "دواء"])
                priority = st.selectbox("الأولوية", ["عادية", "متوسطة", "عالية", "طارئة"])

            address = st.text_area("العنوان", placeholder="العنوان التفصيلي")

            submitted = st.form_submit_button("إضافة المستفيد", use_container_width=True)

            if submitted:
                st.success("تم إضافة المستفيد بنجاح! ✅")
                st.info("سيتم توليد كود QR تلقائيًا للمستفيد")

    with tab3:
        st.markdown("### 📊 تقرير التوزيع")

        # بيانات وهمية للتقرير
        report_data = pd.DataFrame({
            'اسم المستفيد': ['أحمد محمد', 'فاطمة علي', 'محمد أحمد', 'سارة خالد', 'عبد الله يوسف'],
            'رقم الهوية': ['123456789', '987654321', '456789123', '789123456', '321654987'],
            'نوع المساعدة': ['طرد غذائي', 'ملابس', 'طرد غذائي', 'مساعدة نقدية', 'دواء'],
            'تاريخ التوزيع': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
            'الحالة': ['تم التوزيع', 'تم التوزيع', 'تم التوزيع', 'تم التوزيع', 'تم التوزيع']
        })

        st.dataframe(report_data, use_container_width=True)

        # زر التصدير
        csv = report_data.to_csv(index=False)
        st.download_button(
            label="📥 تصدير كـ Excel",
            data=csv,
            file_name='tawzi3_report.csv',
            mime='text/csv'
        )


# صفحة التواصل
def contact_page():
    st.markdown("## 📞 تواصل معنا")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="form-container">
            <h3>📧 معلومات التواصل</h3>
            <p><strong>📧 البريد الإلكتروني:</strong> tawzi3.app@gmail.com</p>
            <p><strong>📱 واتساب:</strong> +972-XXX-XXXXXX</p>
            <p><strong>📍 الموقع:</strong> غزة - فلسطين</p>
            <p><strong>🌐 وسائل التواصل:</strong></p>
            <p>• فيسبوك: /Tawzi3App</p>
            <p>• تليجرام: @Tawzi3App</p>
            <p>• لينكدإن: /company/tawzi3</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 📥 اطلب نسخة تجريبية")

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
                st.success("تم إرسال طلبك بنجاح! سنتواصل معك خلال 24 ساعة ✅")
                st.balloons()


# صفحة المطور
def developer_page():
    st.markdown("## 🧑‍💻 من المطوّر؟")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white; margin-bottom: 2rem;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">👨‍💻</div>
            <h3>إبراهيم صالحة</h3>
            <p>مطوّر تطبيقات سطح المكتب</p>
            <p>📍 غزة - فلسطين</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>💚 رسالة من المطور</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
            أنا إبراهيم صالحة، مطوّر تطبيقات سطح مكتب من غزة. 
            أعمل على تطوير أدوات بسيطة، لكنها فعّالة، لحل مشاكل واقعية في مجتمعنا.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8;">
            <strong>Tawzi3</strong> هو مشروعي لخدمة الناس، وأتمنى أن أسمع ملاحظاتكم 
            واقتراحاتكم للتطوير. هدفي هو جعل عملية توزيع المساعدات أكثر كرامة وفعالية.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # قسم التحديثات القادمة
    st.markdown("## 🔄 التحديثات القادمة")

    updates = [
        ("🌐", "دعم التوزيع عبر الشبكة", "ربط عدة أجهزة في شبكة واحدة"),
        ("👥", "نظام صلاحيات المستخدمين", "إدارة متقدمة للمستخدمين والأدوار"),
        ("☁️", "نسخة سحابية", "عند توفر الإنترنت المستقر"),
        ("📊", "تحليلات متقدمة", "تقارير ذكية ومؤشرات الأداء"),
        ("🔔", "نظام الإشعارات", "تنبيهات للمواعيد والأحداث المهمة"),
        ("🌍", "دعم لغات متعددة", "الإنجليزية والفرنسية بالإضافة للعربية")
    ]

    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(updates):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div style="font-size: 2rem; margin-left: 1rem;">{icon}</div>
                    <div>
                        <h4 style="margin: 0; color: #667eea;">{title}</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">{desc}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# التنقل الرئيسي
def main():
    # القائمة الجانبية
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; color: white; margin-bottom: 2rem;">
        <h2>🟩 Tawzi3</h2>
        <p>نظام توزيع المساعدات الذكي</p>
    </div>
    """, unsafe_allow_html=True)

    # قائمة التنقل
    page = st.sidebar.selectbox(
        "اختر الصفحة",
        ["🏠 الصفحة الرئيسية", "🚀 المميزات", "🌍 الفوائد", "📱 العرض التوضيحي", "📞 تواصل معنا", "🧑‍💻 المطور"],
        index=0
    )

    # معلومات سريعة في الشريط الجانبي
    st.sidebar.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
        <h4 style="color: white; margin-bottom: 1rem;">📊 إحصائيات سريعة</h4>
        <p style="color: white; margin: 0.5rem 0;">⚡ 5 ثوانٍ لكل عملية</p>
        <p style="color: white; margin: 0.5rem 0;">🔒 100% أمان البيانات</p>
        <p style="color: white; margin: 0.5rem 0;">📱 عمل بدون إنترنت</p>
        <p style="color: white; margin: 0.5rem 0;">🆓 نسخة تجريبية مجانية</p>
    </div>
    """, unsafe_allow_html=True)

    # رابط سريع للتحميل
    st.sidebar.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="#" class="custom-button">
            📥 اطلب نسخة تجريبية
        </a>
    </div>
    """, unsafe_allow_html=True)

    # عرض الصفحة المختارة
    if page == "🏠 الصفحة الرئيسية":
        main_page()
    elif page == "🚀 المميزات":
        features_page()
    elif page == "🌍 الفوائد":
        benefits_page()
    elif page == "📱 العرض التوضيحي":
        demo_page()
    elif page == "📞 تواصل معنا":
        contact_page()
    elif page == "🧑‍💻 المطور":
        developer_page()

    # الفوتر
    st.markdown("""
    <div class="footer">
        <h3>🟩 Tawzi3 - نظام توزيع المساعدات الذكي</h3>
        <p>طُور بـ ❤️ في غزة - فلسطين</p>
        <p style="margin-top: 1rem;">
            📧 tawzi3.app@gmail.com | 📱 +972-XXX-XXXXXX
        </p>
        <p style="margin-top: 1rem; opacity: 0.8;">
            © 2024 Tawzi3 - جميع الحقوق محفوظة
        </p>
    </div>
    """, unsafe_allow_html=True)


# تشغيل التطبيق
if __name__ == "__main__":
    main()